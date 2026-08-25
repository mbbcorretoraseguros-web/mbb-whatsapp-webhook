import os
from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = os.environ.get("MYTOKEN", "mbb_webhook_2026")

@app.route("/webhook", methods=["GET"])
def verificar():
    modo = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    desafio = request.args.get("hub.challenge")
    if modo == "subscribe" and token == VERIFY_TOKEN:
        return desafio, 200
    return "Token invalido", 403

@app.route("/webhook", methods=["POST"])
def receber():
    dados = request.get_json(force=True, silent=True) or {}
    print("MENSAGEM RECEBIDA:", dados)
    return "OK", 200

@app.route("/", methods=["GET"])
def home():
    return "Webhook MBB ativo - somente recebimento", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
