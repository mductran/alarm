from flask import request, render_template
from app import app
import os
import requests


@app.route('/', methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        
        response = requests.get("http://10.247.169.41:5000")
        print(response.json()['mode'])

        with app.open_resource("static/ip.txt") as f:
            ip = f.readline().decode("ascii")
        with app.open_resource("static/notification.txt") as f:
            notification = f.readline().decode("ascii")
        return render_template("home.html", ip=ip, mode=response.json()['mode'], notification=notification)

    if request.method == "POST":
        print('request data: ', request.form)
        print('request data: {}, {}'.format(request.form['mode'], request.form['notification']))

        with open(os.path.join(app.root_path, "static/notification.txt"), "r+") as f:
            f.write(request.form["notification"])
            f.seek(0)
            print(f.read())

        return "notification received"
