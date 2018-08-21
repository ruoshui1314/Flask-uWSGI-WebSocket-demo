#!/usr/bin/env python
from flask import Flask, render_template
from flask_uwsgi_websocket import GeventWebSocket

app = Flask(__name__)
ws = GeventWebSocket(app)

@app.route('/')
def index():
    return render_template('index.html')

@ws.route('/websocket')
def echo(ws):
    while True:
        msg = ws.receive()
        print(msg)
        if msg is not None and len(msg):
            from chat_manager import SUBSCRIBER, CHANNEL
            SUBSCRIBER.register(ws, CHANNEL.CHAT)
            SUBSCRIBER.publish(CHANNEL.CHAT, msg)
        elif msg is None: return

if __name__ == '__main__':
    app.run(debug=True, gevent=100)