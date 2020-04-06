from app import application
from flask import request

description = "Uppercase your text"

@application.route("/uppercase", methods=["POST"])
def uppercase():
        content = request.json

        word = content['word']
        result = word.upper()

        return {
            "result": result
        }