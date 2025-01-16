from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/startChat")
def startChat():
    return render_template("chat.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404