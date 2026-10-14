"""Copy only current, generated publication files into the Pages artifact."""
from datetime import date, datetime
import hashlib
import json
from pathlib import Path, PurePosixPath
import shutil
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / '_site'
STATIC = {
    '.nojekyll', 'robots.txt', 'sitemap.xml', 'feed.xml', 'en/feed.xml',
    'fr/feed.xml', 'assets/site.css', 'assets/site.js', 'assets/favicon.svg',
    'images/me.jpeg',
}


def publication_path(name):
    path = PurePosixPath(name)
    if path.is_absolute() or '..' in path.parts or '\\' in name:
        raise ValueError('Unsafe publication path')
    target = ROOT.joinpath(*path.parts)
    if any(parent.is_symlink() for parent in [target, *target.parents] if parent != ROOT.parent):
        raise ValueError('Publication paths must not be symlinks')
    if not target.resolve().is_relative_to(ROOT) or not target.is_file():
        raise ValueError('Missing publication file')
    return target


def main():
    manifest = json.loads((ROOT / 'blog-manifest.json').read_text(encoding='utf-8'))
    today = datetime.now(ZoneInfo('Europe/Paris')).date()
    if manifest.get('origin') != 'https://roukmoute.github.io' or manifest.get('timezone') != 'Europe/Paris':
        raise ValueError('Unexpected publication origin or timezone')
    if manifest.get('previewDrafts') is not False or 'repository' in manifest:
        raise ValueError('Private source or preview metadata cannot be deployed')
    if date.fromisoformat(manifest['asOf']) > today:
        raise ValueError('A future preview cannot be deployed')
    if any(date.fromisoformat(article['publishedAt']) > today for article in manifest['articles']):
        raise ValueError('A future article cannot be deployed')
    assets = {asset['path']: asset for asset in manifest['assets']}
    if set(assets) != STATIC:
        raise ValueError('Unexpected publication assets')
    pages = set(manifest['pages'])
    if not all(name.endswith('.html') for name in pages):
        raise ValueError('Unexpected publication pages')
    names = pages | STATIC | {'blog-manifest.json'}
    for name in names:
        path = publication_path(name)
        if name in assets:
            record = assets[name]
            if path.stat().st_size != record['bytes'] or hashlib.sha256(path.read_bytes()).hexdigest() != record['sha256']:
                raise ValueError('Publication asset differs from verified inventory')
    if OUTPUT.exists():
        raise ValueError('Pages artifact directory must be new')
    for name in sorted(names):
        target = OUTPUT / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(publication_path(name), target)
    print(f'Prepared {len(names)} publication files and {len(manifest["articles"])} articles.')


if __name__ == '__main__':
    main()
