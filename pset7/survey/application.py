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
    # Check if any amongst input fields were empty
    if not request.form.get("name") or not request.form.get("group") or not request.form.get("gender") or not request.form.get("phone"):
        return render_template("error.html", message="Please provide all required information")
    else:
        return render_template("error.html", message="Thank You!")


@app.route("/sheet", methods=["GET"])
def get_sheet():
    return render_template("error.html", message="TODO")
