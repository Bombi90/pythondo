from app import application
from flask import request

description = "This is a description for the hello route"

@application.route("/hello", methods=['POST', 'GET'])
def hello():
    if request.method == 'POST':
            content = request.json
            data = content['data']
            return data
    else:
            searchword = request.args.get('key', '')
            return {
                    "search_word": searchword
            }