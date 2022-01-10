from flask import request, render_template
from app import app
import os


@app.route('/', methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        with app.open_resource("static/ip.txt") as f:
            ip = f.readline().decode("ascii")
        with app.open_resource("static/mode.txt") as f:
            mode = f.readline().decode("ascii")
        with app.open_resource("static/notification.txt") as f:
            notification = f.readline().decode("ascii")
        return render_template("home.html", ip=ip, mode=mode, notification=notification)

    if request.method == "POST":
        print('request data: ', request.form)
        print('request data: {}, {}'.format(request.form['mode'], request.form['notification']))

        with open(os.path.join(app.root_path, "static/ip.txt"), "r+") as f:
            f.write(request.form['addr'])
            f.seek(0)
            print(f.read())
        with open(os.path.join(app.root_path, "static/mode.txt"), "r+") as f:
            f.write(request.form["mode"])
            f.seek(0)
            print(f.read())
        with open(os.path.join(app.root_path, "static/notification.txt"), "r+") as f:
            f.write(request.form["notification"])
            f.seek(0)
            print(f.read())            
        return "connected"


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
