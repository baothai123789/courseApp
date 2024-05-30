from . import app
from flask import render_template, redirect


@app.route("/")
def root():
    return render_template('home.html')


@app.route("/home")
def home():
    redirect("/")


