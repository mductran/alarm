from flask import request, render_template
from app import app

@app.route('/', methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        with app.open_resource("static/ip.txt") as f:
            for line in f:
                pass
            ip = line
        return render_template("home.html", ip=ip)

    if request.method == "POST":
        with app.open_resource("static/ip.txt") as f:
            f.write(request.addr)
        with app.open_resource("static/mode.txt") as f:
            f.write(request.args.get("mode"))
        return "raspberry pi connected successfully"


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
