These files power ocr.html (Image to Text). They run in the visitor's browser; nothing is uploaded.

  tesseract.min.js, worker.min.js        tesseract.js 7.0.0         Apache-2.0  https://github.com/naptha/tesseract.js
  core/tesseract-core-*-lstm.wasm.js     tesseract.js-core 7.0.0    Apache-2.0  https://github.com/naptha/tesseract.js-core
  lang/eng.traineddata.gz                @tesseract.js-data/eng 1.0.0 (4.0.0_best_int)  Apache-2.0  https://github.com/naptha/tessdata

Two core builds are kept: the browser picks relaxed-SIMD or plain SIMD. Browsers without WebAssembly SIMD
(roughly before 2021) are not supported. To update: npm pack the three packages above and copy the same files.
