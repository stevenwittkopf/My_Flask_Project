from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def welcome() -> str:
    return "Welcome to my simple application!"


@app.route("/date")
def date() -> str:
    now = datetime.now()
    return f"This page is being served at {now}"
