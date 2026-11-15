import os
import re
import tempfile

from flask import Flask, request, send_file, render_template_string, abort
import yt_dlp

app = Flask(__name__)

URL_RE = re.compile(r"^https?://(www\.)?instagram\.com/(p|reel|reels|tv)/[\w-]+", re.I)

PAGE = """<!doctype html>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Instagram Video Downloader</title>
<style>
  body{font:16px system-ui,sans-serif;max-width:520px;margin:12vh auto;padding:0 16px;text-align:center}
  input{width:100%;box-sizing:border-box;padding:12px;font-size:16px;border:1px solid #bbb;border-radius:8px}
  button{margin-top:12px;padding:12px 24px;font-size:16px;border:0;border-radius:8px;background:#e1306c;color:#fff;cursor:pointer}
  .err{color:#b00020;margin-top:16px}
  small{color:#777;display:block;margin-top:24px}
</style>
<h1>Instagram Video Downloader</h1>
<form method="post" action="/download">
  <input name="url" type="url" required autofocus
         placeholder="Paste an Instagram reel/post link"
         value="{{ url or '' }}">
  <button>Download</button>
</form>
{% if error %}<p class="err">{{ error }}</p>{% endif %}
<small>Public posts only. Only download content you have the right to save.</small>
"""


@app.get("/")
def index():
    return render_template_string(PAGE)


@app.post("/download")
def download():
    url = request.form.get("url", "").strip()
    if not URL_RE.match(url):
        return render_template_string(
            PAGE, url=url, error="That doesn't look like an Instagram post/reel link."
        ), 400

    tmp = tempfile.mkdtemp()
    opts = {
        "outtmpl": os.path.join(tmp, "%(id)s.%(ext)s"),
        "format": "best[ext=mp4]/best",
        "quiet": True,
        "noplaylist": True,
    }
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(url, download=True)
            path = ydl.prepare_filename(info)
    except Exception:
        return render_template_string(
            PAGE, url=url,
            error="Couldn't download that. It may be private, or Instagram blocked the request.",
        ), 502

    if not os.path.exists(path):
        abort(500)
    return send_file(path, as_attachment=True, download_name=os.path.basename(path))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
