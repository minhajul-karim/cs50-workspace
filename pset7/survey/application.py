# import cs50
import csv
import os.path

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

    # Check if the file already exists
    file_exists = os.path.isfile('survey.csv')
    
    # Save from info into csv file
    with open('survey.csv', 'a', newline='') as csvfile:
        fieldnames = ['Name', 'Blood Group', 'Gender', 'Phone']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header if the file doesn't exist
        if not file_exists:
            writer.writeheader()

        writer.writerow({'Name': name, 'Blood Group': group, 'Gender': gender, 'Phone': phone})

    # Redirect to sheet route
    return redirect('/sheet')


@app.route("/sheet", methods=["GET"])
def get_sheet():
    with open('survey.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return render_template("sheet.html", reader=reader)
    return render_template("error.html", message="CSV file doesn't exist!")
