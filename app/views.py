from flask import render_template
from app import app

@app.route("/")
@app.route("/home")
def home():
    user = {"username": "Helen"}
    posts = [
        {
            "author": {"username": "little blue"},
            "body": "I couldn't beat the Path of Pain..."
        },
        {
            "author": {"username": "CrazyEighty8"},
            "body": "Can someone please help my girlfriend regain her sanity?"
        }
    ]
    return render_template("home.html", title="Home", user=user, posts=posts)