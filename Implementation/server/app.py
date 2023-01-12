from flask import Flask, request, render_template
import pyrebase4

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


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def basic():
    if request.method == 'POST':
        if request.form['submit'] == 'add':

            name = request.form['name']
            db.child("todo").push(name)
            todo = db.child("todo").get()
            to = todo.val()
            return render_template('index.html', t=to.values())
        elif request.form['submit'] == 'delete':
            db.child("todo").remove()
        return render_template('index.html')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
