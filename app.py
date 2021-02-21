import json
from flask import Flask, request, jsonify
import ftx



app = Flask("__main__")

client = ftx.FtxClient('mt6q3o7aheFH89_GMdZUZXf8JbLfJ8oynNRWOIbM','inl1LzA10irNDSb17wABqwFVot0mkx84QumaAsiL', 'test')

@app.route("/")
def get_positions():
    client = ftx.FtxClient('mt6q3o7aheFH89_GMdZUZXf8JbLfJ8oynNRWOIbM','inl1LzA10irNDSb17wABqwFVot0mkx84QumaAsiL', 'test')
    return {'helol', client}

@app.route("/positions")
def get_positions():
    client = ftx.FtxClient('mt6q3o7aheFH89_GMdZUZXf8JbLfJ8oynNRWOIbM','inl1LzA10irNDSb17wABqwFVot0mkx84QumaAsiL', 'test')
    return {'positions':client.get_positions()}

@app.route("/wallet")
def get_wallet_info():
    client = ftx.FtxClient('mt6q3o7aheFH89_GMdZUZXf8JbLfJ8oynNRWOIbM','inl1LzA10irNDSb17wABqwFVot0mkx84QumaAsiL', 'test')
    return {'wallet':client.get_wallet_info()}

@app.route("/balances")
def get_balances():
    client = ftx.FtxClient('mt6q3o7aheFH89_GMdZUZXf8JbLfJ8oynNRWOIbM','inl1LzA10irNDSb17wABqwFVot0mkx84QumaAsiL', 'test')
    return {'balances':client.get_balances()}

@app.route("/futures")
def get_futures():
    client = ftx.FtxClient('mt6q3o7aheFH89_GMdZUZXf8JbLfJ8oynNRWOIbM','inl1LzA10irNDSb17wABqwFVot0mkx84QumaAsiL', 'test')
    return {'futures':client.get_futures()}

