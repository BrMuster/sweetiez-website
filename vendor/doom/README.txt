DOOM for the Play tab in plot.html (the "Doom" button).

engine.js  The game, a TypeScript port, bundled with the libraries it needs into one script.
           It sets window.DoomTS. Source: the npm package @reinbert/doom-ts 0.1.0 (GPL-3.0),
           which is DOOM.ts by Thomas Chandelle, itself from id Software's DOOM (GPL v2).
           Bundled libraries: three, dexie, smplr, lil-gui, stats.js (all MIT).
           Rebuilt with:  bun build entry.js --minify --target=browser --format=iife
           where entry.js is:  import { Doom } from "@reinbert/doom-ts"; window.DoomTS = Doom;
wad.js     The shareware game data (doom1.wad, episode 1), which id Software allows anyone to
           redistribute unmodified. Raw-deflate compressed and base64 encoded, assigned to
           window.DOOM_WAD_Z, so that it also loads when plot.html is opened straight from disk.
COPYING.txt  The licence text that came with the port.

plot.html loads both files the first time the Doom button is pressed, so they cost nothing until then.
Mouse look uses the browser's pointer lock (the page asks for it when you click the game).
Sound effects work. The music is switched off: the port downloads its instruments from
gleitz.github.io, and plot.html's Content-Security-Policy (connect-src) deliberately blocks that.
