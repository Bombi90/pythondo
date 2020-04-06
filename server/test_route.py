from app import application
from flask import request

description = "This page is used to calculate a test and returns a number as result"

@application.route("/test", methods=["POST"])
def test():
        content = request.json
        
        number = content['number']
        # IL TUO CODICE PER FARE FATTORIALE
        result = number + number

        return {
            "result": result
        }