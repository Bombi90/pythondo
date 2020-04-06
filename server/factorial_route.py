from app import application
from flask import request

description = "This page is used to calculate a factorial and returns a number as result"

@application.route("/factorial", methods=["POST"])
def fuctorial():
        content = request.json
        number = content['number']
        # IL TUO CODICE PER FARE FATTORIALE
        result = number + number
        return {
            "result": result
        }