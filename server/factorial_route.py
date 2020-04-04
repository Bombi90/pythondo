from app import application
from flask import request

@application.route("/factorial", methods=["POST"])
def fuctorial():
        content = request.json
        number = content['number']
        # IL TUO CODICE PER FARE FATTORIALE
        result = number + number
        return {
            "cane": result
        }