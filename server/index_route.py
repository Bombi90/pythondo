from app import application
from flask import request, render_template

@application.route("/")
def index():
    return render_template('index.html', message="HOLA")