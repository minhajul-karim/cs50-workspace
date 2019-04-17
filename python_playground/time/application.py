from flask import Flask
from datetime import datetime
from pytz import timezone

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.now(timezone('Asia/Dhaka'))
    return "The current time of Dhaka, Bangladesh is {}".format(now)

@app.route("/something")
def not_found():
    return "ERROR 404 - NOT FOUND"


@app.route("/show/<number>")
def show_num(number):
    return "You have enterned {}".format(number)