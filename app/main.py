from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, World to address {}!\n".format(request.remote_addr)


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


if __name__ == "__main__":
    app.run()