from flask import request
from app import app


@app.route('/')
def hello():
    return "Hello, World to address {}!\n".format(request.remote_addr)

@app.route('/ip', methods=["POST"])
def register_phone(ip=""):
    if request.method == "POST":
        with open("app/phone_ip.txt", "w+") as f:
            f.write(ip+"\n")

@app.route("/mode", methods=["GET", "POST"])
def changeMode(mode=""):
    if request.method == "GET":
        return "current mode\n"
    elif request.method == "POST":
        return "changing mode\n"


@app.route('/notification', methods=["GET", "POST"])
def notify(message=""):
    # get all notifications
    if request.method == "GET":
        return "all notifications"
    elif request.method == "POST":
        return "receving signal"
