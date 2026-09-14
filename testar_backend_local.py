import http.server, json

PORT = 8080
state = {
    "config": {
        "status_forno": "saindo_agora",
        "pao_destaque_hoje": "Sourdough Tradicional Demeter",
        "proxima_fornada": "Saindo Agora!",
        "alerta_ativo": True,
        "alerta_texto": "🔥 Fornada de Sourdough Demeter saindo agora!",
        "ultima_atualizacao": "2026-09-14 10:30:00"
    }
}

class Handler(http.server.BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self):
        self.send_response(200); self._cors(); self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json"); self._cors(); self.end_headers()
        self.wfile.write(json.dumps({"success": True, "data": state}).encode("utf-8"))
        print(" -> [GET] Site leu as fornadas com sucesso!")

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8")
        data = json.loads(body)
        if data.get("config"):
            state["config"].update(data["config"])
            print(f" -> [POST] 🔥 FORNADA ATUALIZADA: {state['config']['pao_destaque_hoje']} ({state['config']['proxima_fornada']})")
        self.send_response(200)
        self.send_header("Content-Type", "application/json"); self._cors(); self.end_headers()
        self.wfile.write(json.dumps({"success": True, "message": "Fornada atualizada!"}).encode("utf-8"))

print(f" Servidor de Teste do Backend rodando em http://localhost:{PORT}")
print("Para testar no PWA, cole http://localhost:8080 nas configurações ⚙️ do app.")
http.server.HTTPServer(("", PORT), Handler).serve_forever()
