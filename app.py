import json
from flask import Flask, request, jsonify
import ftx



app = Flask("__main__")

client = ftx.FtxClient('mt6q3o7aheFH89_GMdZUZXf8JbLfJ8oynNRWOIbM','inl1LzA10irNDSb17wABqwFVot0mkx84QumaAsiL', 'test')

@app.route("/")
def hello():
    return 'helol'

@app.route("/webhook", methods=['POST'])
def webhook():
    if data['side'].upper() == "BUY":
        client.place_order('ETH/USD', 'buy', None, 1, 'market')
        return 'buy'
    else:
        client.place_order('ETH/USD', 'sell', None, 0.005, 'market')
        return 'sell'


