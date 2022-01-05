from flask import request, render_template
from app import app

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
        with app.open_resource("static/ip.txt") as f:
            f.write(request.addr)
        with app.open_resource("static/mode.txt") as f:
            f.write(request.args.get("mode"))
        with app.open_resource("static/notification") as f:
            f.write(request.args.get("notification"))
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
