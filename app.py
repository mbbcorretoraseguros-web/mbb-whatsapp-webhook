import os
from flask import Flask, request

app = Flask(__name__)

# Token de verificacao - usa a variavel MYTOKEN do Render, com fallback
VERIFY_TOKEN = os.environ.get('MYTOKEN', 'mbb_webhook_2026')

@app.route('/')
def home():
    return 'Servidor da MBB rodando!'

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # GET = verificacao da Meta (nao alterar)
    if request.method == 'GET':
        token = request.args.get('hub.verify_token')
        if token == VERIFY_TOKEN:
            return request.args.get('hub.challenge')
        return 'Token invalido', 403

    # POST = recebimento de mensagens (nao alterar)
    elif request.method == 'POST':
        data = request.get_json(silent=True)
        print('MENSAGEM RECEBIDA:', data)
        return 'OK', 200

@app.route('/privacy')
def privacy():
    return """<html><body style="font-family:Arial;max-width:700px;margin:40px auto;padding:0 20px">
<h1>Política de Privacidade</h1>
<p>Este aplicativo é utilizado pela MBB Corretora de Seguros para receber e
processar mensagens enviadas via WhatsApp Business API.</p>
<h2>Dados coletados</h2>
<p>Número de telefone do remetente e conteúdo das mensagens trocadas,
utilizados exclusivamente para atendimento e gestão de serviços de seguros.</p>
<h2>Armazenamento e uso</h2>
<p>Os dados são tratados de forma confidencial, conforme a legislação vigente
(LGPD), e utilizados apenas para finalidades de atendimento ao cliente e
operações da corretora.</p>
<h2>Contato</h2>
<p>Para dúvidas ou solicitações, entre em contato com a MBB Corretora de Seguros.</p>
</body></html>"""

@app.route('/terms')
def terms():
    return """<html><body style="font-family:Arial;max-width:700px;margin:40px auto;padding:0 20px">
<h1>Termos de Serviço</h1>
<p>Este serviço processa mensagens recebidas via WhatsApp para atendimento
da MBB Corretora de Seguros. Ao enviar uma mensagem, o usuário concorda
com o tratamento dos dados para finalidades de atendimento.</p>
</body></html>"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
