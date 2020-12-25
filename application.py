import os
import requests

from flask import Flask, jsonify, render_template, request,session
from flask_session import Session
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/main")
def main():
    # username= request.form.get("username")
    # roomid= request.form.get("roomid")
    username= request.args.get("username")
    roomid= request.args.get("roomid")
    if username and roomid:
        return render_template('main.html',username=username,roomid=roomid)
    else:
        return render_template('index.html')

@socketio.on("submit message")
def chat(data):
    message = data["message"]
    emit("announce vote", {'message':message} , broadcast=True)
