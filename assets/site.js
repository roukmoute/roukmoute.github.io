"use strict";
(() => {
  const compatibility = document.querySelector("[data-redirect-target]");
  if (compatibility) {
    try {
      const current = new URL(window.location.href);
      const destination = new URL(compatibility.dataset.redirectTarget, current);
      if (!['http:', 'https:'].includes(destination.protocol) || destination.origin !== current.origin || destination.username || destination.password || destination.pathname.startsWith('/fr/') || destination.pathname === current.pathname) return;
      destination.search = current.search;
      destination.hash = current.hash;
      const fallback = compatibility.querySelector("[data-redirect-link]");
      if (fallback) fallback.href = destination.pathname + destination.search + destination.hash;
      window.location.replace(destination.href);
    } catch { /* The visible link remains available if the address is invalid. */ }
    return;
  }
  for (const link of document.querySelectorAll("[data-language-link]")) {
    const original = link.getAttribute("href");
    function updateLink() {
      const destination = new URL(original, window.location.origin);
      if (destination.origin !== window.location.origin || destination.username || destination.password) return;
      destination.search = window.location.search;
      let anchor;
      try { anchor = decodeURIComponent(window.location.hash.slice(1)); }
      catch { anchor = window.location.hash.slice(1); }
      let anchors = {};
      try { anchors = JSON.parse(link.dataset.anchorMap || "{}"); }
      catch { /* The plain link remains usable without a translated fragment. */ }
      if (anchor) destination.hash = Object.hasOwn(anchors, anchor) ? anchors[anchor] : anchor;
      link.href = destination.pathname + destination.search + destination.hash;
    }
    link.addEventListener("click", updateLink);
    link.addEventListener("auxclick", updateLink);
    window.addEventListener("hashchange", updateLink);
    updateLink();
  }
})();
