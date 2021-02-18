from flask import Flask, jsonify
from flask import request
from flask_cors import CORS, cross_origin

app = Flask(__name__)

FRONTEND_URL = "http://localhost:3001/"

CORS(app, origins=[FRONTEND_URL])

app.config["CORS_HEADERS"] = "Content-Type"
app.config["CORS_SEND_WILDCARD"] = True






if __name__ == "__main__":
    app.run(debug=True)