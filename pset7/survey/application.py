# import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():

    # Information posted by form
    name = request.form.get("name")
    group = request.form.get("group")
    gender = request.form.get("gender")
    phone = request.form.get("phone")

    # Input validation for form inputs
    if not name or not group or not gender or not phone:
        return render_template("error.html", message="Please provide all required information")
    
    # Save from info into csv file
    with open('survey.csv', 'a', newline='') as csvfile:
        fieldnames = ['user_name', 'blood_group', 'user_gender', 'user_phone']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        #writer.writeheader()
        writer.writerow({'user_name': name, 'blood_group': group, 'user_gender': gender, 'user_phone': phone})

    return render_template("success.html")


@app.route("/sheet", methods=["GET"])
def get_sheet():
    return render_template("error.html", message="TODO")
