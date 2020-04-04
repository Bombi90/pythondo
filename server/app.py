from flask import Flask
import os

application = Flask(__name__)
@application.route("/")
def hello():
    return "Hello World 28"
if __name__ == "__main__":
    application.run(host="0.0.0.0", port=int(os.getenv("PORT")))

    