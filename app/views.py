from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User

@app.route("/")
@app.route("/home")
@login_required
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
    return render_template("home.html", title="Home", posts=posts)

@app.route("/login", methods=["GET", "POST"])
def login():
    # If user is logged in, redirect to home page.
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        # Two error conditions: invalid username, incorrect password
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            redirect(url_for("home"))
        return redirect(next_page)
    return render_template("login.html", title="Sign In", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user!")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)