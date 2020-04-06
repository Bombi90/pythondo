from app import application
from flask import request

description = ""

@application.route("/route_name", methods=["POST"])
def function_name():
        content = request.json
        

        result = ""

        return {
            "result": result
        }