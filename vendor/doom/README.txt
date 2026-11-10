DOOM for the Play tab in plot.html (the "Doom" button).

doom.js holds the DOOM engine and its shareware game data (episode 1) as one WebAssembly
module, raw-deflate compressed and base64 encoded. plot.html loads it the first time the
Doom button is pressed, so it costs nothing until then.

Source: the doom.wasm in the npm package wasm-doom 1.2.0 (MIT), which copies it from
https://github.com/diekmann/wasm-fizzbuzz (Cornelius Diekmann).
DOOM is by id Software, released under the GNU GPL v2. The shareware data may be freely
redistributed unmodified.

To rebuild: raw-deflate doom.wasm, base64 it, and assign it to window.DOOM_WASM_Z.
