from flask import (Blueprint, render_template,
                     redirect, url_for, request,
                     flash, abort)
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from myproject import db, app
from myproject.models import User
from myproject.auth.forms import LoginForm, SignupForm

auth_blueprint = Blueprint('auth',
                           __name__,
                           template_folder='templates/auth')

@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You logged out!')
    return redirect(url_for('index'))

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user is None:
            flash('something wrong!')
            redirect(url_for('auth.login'))
        elif user.check_password(form.password.data):

            login_user(user)

            flash('Logged in successfully.')

            # login => today's schedule page
            return redirect(url_for('index'))
        else:
            pass


    return render_template('login.html', form=form)

@auth_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if form.validate_on_submit():

        if User.query.filter_by(email=form.email.data).first():
            flash('Email has been registered already!')
            redirect(url_for('auth.signup'))


        elif User.query.filter_by(username=form.username.data).first():
            flash('Username has been registered already!')
            redirect(url_for('auth.signup'))

        else:
            user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

            db.session.add(user)
            db.session.commit()
            flash('Now You can login!')
            return redirect(url_for('auth.login'))
    return render_template('signup.html', form=form)