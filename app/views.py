from flask import request, render_template
from app import app


@app.route('/', methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        # ip = ""
        # mode = ""
        # with open("./pi_ip.txt", "r") as f:
        #     for line in f:
        #         pass
        #     ip = line
        # with open("./mode.txt", "r") as f:
        #     for line in f:
        #         pass
        #     mode = line
        return render_template("home.html")

    if request.method == "POST":
        addr = request.args.get("address")
        mode = request.args.get("mode")
        print("addr: {} \n mode: {}".format(addr, mode))
        with open("pi_ip.txt", "w") as f:
            f.write(addr)
        with open("pi_ip.txt", "w") as f:
            f.write(mode)
        return "raspberry pi connected successfully"


@app.route("/mode", methods=["GET", "POST"])
def changeMode(mode=""):
    if request.method == "GET":
        return "current mode\n"
    elif request.method == "POST":
        return "changing mode\n"


@app.route('/notification', methods=["GET", "POST"])
def notify(message=""):
    # get all notifications
    with open('filename.txt') as f:
        for line in f:
            pass
        last_line = line
    if request.method == "GET":
        return "all notifications", 200
    elif request.method == "POST":
        return "receving signal", 200
