from flask import Flask
from flask_sock import Sock
import json

app = Flask(__name__)
sock = Sock(app)

connetions = {}
@sock.route('/connect')
def socketRoute(ws):
    userid = None
    while True:
        data = ws.receive()
        dados = json.loads(data)


        if dados['type'] == 'createConnection':
            userid = dados['sendId']
            connetions[str(userid)] = ws
        if dados['type'] == 'sendMensage':
            if dados['receivedId'] in connetions:
                connetions[dados['receivedId']].send(data)

       

app.run(port=2000,host="0.0.0.0",debug=True)