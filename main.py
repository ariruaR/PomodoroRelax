from flask import Flask, redirect, render_template
import time
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/timer", methods=["GET", 'POST'])
def timer():
    return render_template("timer.html")

if __name__ == "__main__":
    app.run(debug=True)