from flask import Blueprint, render_template, request, flash, url_for, redirect, session
from werkzeug.security import check_password_hash
from models.user import User

sessions_blueprint = Blueprint("sessions", __name__, template_folder="templates")

@sessions_blueprint.route('/')
def login():
    return render_template('sessions/login.html')

@sessions_blueprint.route('/login-check', methods = ["POST"])
def login_check():
    user = User.get(User.email == request.form['email_input'])
    password_to_check = request.form['password_input']
    hashed_password = user.password
    result = check_password_hash(hashed_password, password_to_check)
    

    if result:
        flash(f"Login successful.")
        session["email"] = request.form['email_input']
        flash(f"{session['email']}")
        return redirect(url_for('sessions.login'))
    else:
        flash(f"Login failure.")
        flash("Email/password is not correct")
        return redirect(url_for('sessions.login'))

    