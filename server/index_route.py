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

        is_blank_page = False
        try:
            is_blank_page = module.is_blank_page
        except:
             is_blank_page = False

        routeName = routeName.replace("_route", "")
        label = routeName.capitalize()
        try: 
            label = module.label
        except:
            pass
                
        urls.append({
            "id": routeName,
            "props": {
                "methods": ["GET", "POST"],
                "description": description,
                "label": label
                
            },
            "isBlank": is_blank_page,
            "link": "/" + routeName
        })


@application.route("/")
def index():
    pythondo = {
        "urls": urls
    }
    return render_template('index.jinja2', pythondo=pythondo)
