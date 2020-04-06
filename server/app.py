from flask import Flask
import os

application = Flask(__name__, static_url_path='/static')
import hello_route
import index_route
import factorial_route
import uppercase_route

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=int(os.getenv("PORT")))
