import os
import smtplib
from flask import Flask, render_template, request, redirect

# Configure app
app = Flask(__name__)

students = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registered", methods=["POST"])
def result():
    name = request.form.get("name")
    group = request.form.get("blood_groups")
    phone = request.form.get("phone")
    email = request.form.get("email")
    sender_email = "rizon2637@gmail.com"
    # password = input("Enter password & press ENTER: ")
    if not name or not group or not phone or not email:
        return render_template("failure.html")
    # else
    students.append("Mr./Mrs. {} has {} blood & his/her num is {}, email: {}".format(name, group, phone, email))
    # Mail content
    message = "You're registered!"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    # server.login(sender_email, os.getenv('PASSWORD'))
    server.login(sender_email, "9898372minhajul") # BAD PRACTICE.
    server.sendmail(sender_email, email, message)
    return redirect("/list")

@app.route("/list")
def all_info():
    return render_template("success.html", all_students = students)