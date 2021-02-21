import json
from flask import Flask, request, jsonify
import ftx



app = Flask("__main__")

client = ftx.FtxClient('mt6q3o7aheFH89_GMdZUZXf8JbLfJ8oynNRWOIbM','inl1LzA10irNDSb17wABqwFVot0mkx84QumaAsiL', 'test')

@app.route("/")
def hello():
    return 'helol'

@app.route("/test")
def get_balances():
    data = json.loads(client.get_balances())
    ff = 'd'
    for b in data: 
        if b['coin'] == 'ETH':
            ff = b['free']
    return ff

