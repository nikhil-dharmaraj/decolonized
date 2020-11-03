import os, csv

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

#Route for the introduction/home page. No POST request necessary here, just rendering the static intro.html template for any incoming GET requests.
@app.route("/")
def intro():
    """Show introduction page"""
    return render_template("intro.html")


#Route for the Histories page. Again, o POST request necessary here, just rendering the index.html template for any incoming GET requests, but with two important parameters:
#info: a list-of-dictionaries version of the main sourcing histories.csv file.
#years: a list of all the years relevant to the file, with repeats removed.
@app.route("/year")
def year():
    """Get decolonization information for a specific year"""
    info = []
    years = []
    with open('histories.csv') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            info.append(row)
            years.append(row['Year'])
        modyears = list(dict.fromkeys(years)) #removing repeats
    return render_template("index.html", info=info, years=modyears)
