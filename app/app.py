import os
import socket
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)
INSTANCE = os.getenv("INSTANCE_NAME", socket.gethostname())
MOVIES = [
    {"title": "Missão Nuvem", "genre": "Aventura", "duration": "1h 42min"},
    {"title": "O Código Perdido", "genre": "Mistério", "duration": "2h 01min"},
    {"title": "Além do Cluster", "genre": "Ficção", "duration": "1h 35min"},
]
HTML = """
<!doctype html><html lang="pt-br"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Jornada Streaming Lab</title>
<style>body{font-family:system-ui;background:#0d172a;color:#f8fafc;max-width:800px;margin:45px auto;padding:20px}
header{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap}
.pill{padding:9px 14px;border-radius:30px;background:#164e63;color:#cffafe}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:16px}
article{background:#1e293b;border:1px solid #334155;border-radius:14px;padding:22px}
button{background:#38bdf8;border:0;padding:12px 18px;border-radius:8px;font-weight:bold;cursor:pointer}
small{color:#cbd5e1}a{color:#7dd3fc}</style></head><body>
<header><div><h1>🎬 Jornada Streaming Lab</h1><p>Catálogo fictício • Docker e balanceamento</p></div><span class="pill">Servidor: <strong>{{ instance }}</strong></span></header>
<h2>Filmes disponíveis</h2><div class="grid">{% for movie in movies %}
<article><div style="font-size:40px">🎞️</div><h3>{{ movie.title }}</h3>
<p>{{ movie.genre }}</p><small>{{ movie.duration }}</small></article>{% endfor %}</div>
<p><button onclick="location.reload()">🔄 Fazer outra requisição</button></p>
<p><small>Atualize a página e veja se outro contêiner respondeu. Isto é apenas o catálogo: não reproduz vídeos nem executa AKS.</small></p>
<p><small>API para testar: <a href="/api/status">/api/status</a></small></p>
</body></html>
"""
@app.get("/")
def home():
    return render_template_string(HTML, movies=MOVIES, instance=INSTANCE)

@app.get("/api/status")
def status():
    return jsonify({"instance": INSTANCE, "movies": len(MOVIES), "message": "Catálogo disponível"})

@app.get("/health")
def health():
    return jsonify({"status": "ok"})
