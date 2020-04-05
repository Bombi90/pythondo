from app import application
from flask import request, render_template
import os
import importlib

entries = os.listdir('./')
urls = []
for filename in entries:
    if "_route" in filename and not("index" in filename):
        routeName = filename.replace(".py", "")
        module = importlib.import_module(routeName)
        description = ""
        try:
            description = module.description
        except:
             description = "No description Available"

        routeName = routeName.replace("_route", "")
        urls.append({
            "id": routeName,
            "props": {
                "methods": ["GET", "POST"],
                "description": description,
                "label": routeName.capitalize(),
            },
            "link": "/" + routeName
        })


@application.route("/")
def index():
    pythondo = {
        "urls": urls
    }
    return render_template('index.html', pythondo=pythondo)
