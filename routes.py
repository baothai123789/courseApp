from . import app
from flask import render_template, redirect,request
from .controller import studentController

@app.route("/")
def root():
    return render_template('home.html')


@app.route("/home")
def home():
    redirect("/")

@app.route("/student/detail/<id>")
def getStudentDetail(id:str):
    student = studentController.getStudent(id)
    return student.detail.username
    


