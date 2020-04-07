
from flask import Blueprint, render_template, request, flash, redirect, url_for, abort
from models.user import User
from flask_login import current_user, login_user



users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')
@users_blueprint.route('/')
def index():
    
    return render_template('home.html')

@users_blueprint.route('/new', methods=['GET'])
def new():
    if not current_user.is_authenticated:
        return render_template('users/new.html')
    else:
        return redirect(url_for('users.index'))

@users_blueprint.route('/receive-sign-up', methods=['POST'])
def create():
    # pass
    username_input = request.form.get('username_input')
    password_input = request.form.get('password_input')
    email_input = request.form.get('email_input')
    # hashed_password = generate_password_hash(password_input)
    user = User(name = username_input, password = password_input, email = email_input)
    if user.save():
        flash(f"Account has been created successful")
        login_user(user)
        return redirect(url_for('users.index'))
        
    else:
        return render_template('users/new.html', errors = user.errors)
    # if name.save():
        # return render_template('users/new.html')
    # else:
    #   return render_template('users/new.html')
    # return render_template('users/new.html')
 

@users_blueprint.route('/<username>', methods=["GET"])
def show(username):
    pass


# @users_blueprint.route('/', methods=["GET"])
# def index():
#     return "USERS"


@users_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass


@users_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass