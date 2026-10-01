#!/usr/bin/env python3
"""Construit la version installable (PWA) dans app/ à partir de index.html.

index.html reste la source unique (c'est aussi la page publiée comme artefact Claude).
Ce script ajoute l'enveloppe HTML complète, le manifeste, le service worker et les icônes.
Usage : python3 tools/build.py
"""
import json, os, struct, zlib, hashlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "app")
os.makedirs(OUT, exist_ok=True)

# ---------- icônes PNG (même logo pixel que l'appli) ----------
BG, TILE = (10, 10, 12), (29, 29, 35)
DOTS = ["#ff5a7a", "#ffd23f", "#4fc3f7", "#7bd88f", "#b48cff", "#ff9f1c"]
hexrgb = lambda h: tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))

def png(size, path):
    cell = size * 0.62 / 8          # le logo occupe le centre (zone sûre des icônes « maskable »)
    off = (size - cell * 8) / 2
    rows = []
    for y in range(size):
        row = bytearray([0])
        for x in range(size):
            cx, cy = (x - off) / cell, (y - off) / cell
            c = BG
            if 0 <= cx < 8 and 0 <= cy < 8:
                c = TILE
                ix, iy = int(cx), int(cy)
                if ix in (1, 3, 5) and iy in (1, 3, 5):
                    c = hexrgb(DOTS[(ix + iy * 3) % len(DOTS)])
            row += bytes(c)
        rows.append(bytes(row))
    raw = zlib.compress(b"".join(rows), 9)
    chunk = lambda t, d: struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d) & 0xffffffff)
    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0))
                + chunk(b"IDAT", raw) + chunk(b"IEND", b""))

for s in (180, 192, 512):
    png(s, os.path.join(OUT, f"icon-{s}.png"))

# ---------- manifeste ----------
shortcut = lambda name, short, h: {"name": name, "short_name": short, "url": f"./#{h}",
                                   "icons": [{"src": "icon-192.png", "sizes": "192x192"}]}
manifest = {
    "name": "Habit Pix", "short_name": "Habit Pix", "lang": "fr",
    "description": "Habitudes, sport et nutrition, style pixel.",
    "start_url": "./", "scope": "./", "display": "standalone", "orientation": "portrait",
    "background_color": "#0a0a0c", "theme_color": "#0a0a0c",
    "icons": [{"src": "icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any maskable"},
              {"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"}],
    "shortcuts": [shortcut("Temps restant", "Temps", "time"), shortcut("Ajouter un repas", "Repas", "food"),
                  shortcut("Séance du jour", "Sport", "sport"), shortcut("Journal", "Journal", "journal")],
}
with open(os.path.join(OUT, "manifest.webmanifest"), "w") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

# ---------- page ----------
src = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
head = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon-192.png">
<link rel="apple-touch-icon" href="icon-180.png">
<meta name="apple-mobile-web-app-title" content="Habit Pix">
</head>
<body>
"""
tail = """
<script>
if("serviceWorker" in navigator) addEventListener("load",()=>navigator.serviceWorker.register("sw.js").catch(()=>{}));
</script>
</body>
</html>
"""
page = head + src + tail
with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
    f.write(page)

# ---------- service worker (hors ligne) ----------
version = hashlib.sha1(page.encode()).hexdigest()[:10]
sw = """// Généré par tools/build.py : garde l'appli disponible hors ligne.
const CACHE="habitpix-%s";
const SHELL=["./","index.html","manifest.webmanifest","icon-180.png","icon-192.png","icon-512.png"];
self.addEventListener("install",e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(SHELL)).then(()=>self.skipWaiting()))});
self.addEventListener("activate",e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener("fetch",e=>{
  const r=e.request;if(r.method!=="GET")return;
  const u=new URL(r.url);
  if(u.origin===location.origin){
    // page : réseau d'abord (pour recevoir les mises à jour), cache si hors ligne
    if(r.mode==="navigate"){e.respondWith(fetch(r).then(res=>{const c=res.clone();caches.open(CACHE).then(x=>x.put("index.html",c));return res}).catch(()=>caches.match("index.html")));return}
    e.respondWith(caches.match(r).then(m=>m||fetch(r)));return;
  }
  if(u.hostname.endsWith("fonts.googleapis.com")||u.hostname.endsWith("fonts.gstatic.com")){
    e.respondWith(caches.open(CACHE).then(c=>c.match(r).then(m=>m||fetch(r).then(res=>{c.put(r,res.clone());return res}))));
  }
});
""" % version
with open(os.path.join(OUT, "sw.js"), "w") as f:
    f.write(sw)
print("app/ construit, version", version)
