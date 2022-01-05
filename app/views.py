from flask import request, render_template
from app import app
import os


@app.route('/', methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        with app.open_resource("static/ip.txt") as f:
            for line in f:
                pass
            ip = line
        with app.open_resource("static/mode.txt") as f:
            for line in f:
                pass
            mode = line
        with app.open_resource("static/notification.txt") as f:
            for line in f:
                pass
            notification = line
        return render_template("home.html", ip=ip, mode=mode, notification=notification)

    if request.method == "POST":
        with open(os.path.join(app.root_path, "static/ip.txt"), "w") as f:
            f.write(request.data['remote_addr'])
        with open(os.path.join(app.root_path, "static/mode.txt"), "w") as f:
            f.write(request.data["mode"])
        with open(os.path.join(app.root_path, "static/notification.txt"), "w") as f:
            f.write(request.data["notification"])
        return render_template("connected")


@app.route("/mode", methods=["GET", "POST"])
def changeMode(mode=""):
    if request.method == "GET":
        with app.open_resource("static/mode.txt") as f:
            for line in f:
                pass
            mode = line
        return mode
    elif request.method == "POST":
        return "changing mode\n"


@app.route('/notification', methods=["GET", "POST"])
def notify(message=""):
    if request.method == "GET":
        return "all notifications", 200
    elif request.method == "POST":
        return "receving signal", 200
