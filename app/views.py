from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me={}".format(
            form.username.data, form.remember_me.data))
        return redirect(url_for("home"))
    return render_template("login.html", title="Sign In", form=form)