from flask import Flask, render_template, flash, request, url_for, redirect
from content_management import Content

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

from dbconnect import conncection

TOPIC_DICT = Content()

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html", TOPIC_DICT = TOPIC_DICT)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.route('/login/', methods = ['GET', 'POST'])
def login_page():
    error = ''
    try:
        if request.method == "POST":
            attempted_username = request.form['username']
            attempted_password = request.form['password']

            # flash(attempted_username)
            # flash(attempted_password)

            if attempted_username == "admin" and attempted_password == 'password':
                return redirect(url_for('dashboard'))
            else:
                error = "Invalid credentials. Try Again. "
        return render_template("login.html", error = error)

    except Exception as e:
        # flash(e)
        return render_template("login.html", error = error)


class RegistrationForm(FlaskForm):
    username = TextField('Username', [validators.Length(min=4, max=20)])
    email = TextField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('New Password', [validators.Required(), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice (updated Jan 22, 2015)', [validators.Required()])

@app.route('/register/', methods = ['GET', 'POST'])
def register_page():
    try:
        c, conn = conncection()
        return("okay")
    except Exception as e:
        return(str(e))

if __name__ == "__main__":
    app.run()
