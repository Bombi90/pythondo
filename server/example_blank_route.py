from app import application
from flask import request
import random

description = "This page is an example of blank route"
label = "BlankRoute"
is_blank_page = True

@application.route("/example_blank", methods=["POST", "GET"])

def example_blank():  
    if request.method == 'GET':
        response = f"""
        <style>
        h1 {{
            color: red
        }}
        </style>
        <script>
        const h1 = document.getElementById("example-hello")
         const post =  async (text) => {{ 
            const response =  await fetch("/example_blank", {{
                        headers: {{ "Content-Type": "application/json" }},
                        method: "POST",
                        body: JSON.stringify({{text}})
            }})
            const data = await response.json()
            document.getElementById("pythondo-app-container").innerHTML = data.html
        }}
        h1.addEventListener("click", async event => {{
            await post(event.target.innerText)
        }})
        </script>
        <h1 id="example-hello">Hello</h1>
        """
        return {
            "html": response
        }
    elif request.method == 'POST':
        content = request.json
        text = content['text']
        return {
            "html": f""" 
            <script></script>
                <h1>{text + "Pythondo"}</h1>
            """
        }