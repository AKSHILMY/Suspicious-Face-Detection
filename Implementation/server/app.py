

import pyrebase
import json

config = {
    "apiKey": "AIzaSyBT50mv3eHbe2l3vir1fl0ucF2wzJKA0fc",
    "authDomain": "labmon-cef2e.firebaseapp.com",
    "databaseURL": "https://labmon-cef2e-default-rtdb.firebaseio.com",
    "projectId": "labmon-cef2e",
    "storageBucket": "labmon-cef2e.appspot.com",
    "messagingSenderId": "957845625948",
    "appId": "1:957845625948:web:25c548aa8363f0e2411a99",
    "measurementId": "G-R6VBLEH2VJ"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

from flask import *

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def getThis():
    if request.method == "POST":
        textInput = request.get_json()
        print(textInput)
        db.child("detections").push(textInput)
        return render_template("index.html")
    else:
        detects = db.child("detections").order_by_key().limit_to_last(1).get()
        detect = detects.val()
        print(type(detect))
        return render_template("index.html",text=detect.values())

@app.route("/result", methods=["GET"])
def getResult():
    detects = db.child("detections").order_by_key().limit_to_last(1).get()
    detect = detects.val()
    print(type(detect))
    print(list(dict(detect).values())[0])
    result = list(dict(detect).values())[0]
    return f"{result}"

if __name__ == '__main__':
    app.run(debug=True)
