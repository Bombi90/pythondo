from app import application
from flask import request

description = "This page is used to check if a number is odd or even"

@application.route("/odd", methods=["POST"])
def odd():
        content = request.json
        number = content['number']
        
        if number%2 == 0:
            return {
            "result": 'The number {} is even' . format(number)
            }
        
        else:
            return {
            "result": 'The number {} is odd' . format(number)
            }