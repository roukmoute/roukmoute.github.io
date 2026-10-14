# Le blog publié de Roukmoute

[English](README.md) · **Français**

Ce dépôt contient les fichiers générés de
[roukmoute.github.io](https://roukmoute.github.io/) et son déploiement Pages.
Le français est le défaut du site, avec une édition anglaise complète sous `/en/`.

Les sources des articles, brouillons et leur historique sont dans le dépôt privé
`roukmoute/blog-sources`. Modifier les contenus et dates de publication là-bas.
Seuls les articles relus, marqués `scheduled` et arrivés à leur date dans
Europe/Paris peuvent être exportés ici. Tous les articles sont actuellement en
brouillon pendant leur réécriture par l'auteur.

Le build privé vérifie les articles publiables chaque mercredi à 10 h 17
Europe/Paris, ainsi qu'après les modifications de main. Une clé de déploiement
dédiée peut modifier ce seul dépôt. Le push public déclenche le workflow Pages,
qui prépare seulement les fichiers générés inventoriés dans `blog-manifest.json`.

Conserver `.github/` et ces README lors de la synchronisation. Ne jamais ajouter
les articles Markdown, l'historique des sources, les aperçus privés ou identifiants.
