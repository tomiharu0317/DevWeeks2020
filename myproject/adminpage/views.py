from flask import (Blueprint, render_template,
                     redirect, url_for, request,
                     flash, abort)
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from myproject import db, app
from myproject.models import AdminUser
from myproject.adminpage.forms import LoginForm, SignupForm

admin_blueprint = Blueprint('adminpage',
                           __name__,
                           template_folder='templates/adminpage')

@admin_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You logged out!')
    return redirect(url_for('index'))

@admin_blueprint.route('/login', methods=['GET', 'POST'])
def login():


    form = LoginForm()
    if form.validate_on_submit():

        user = AdminUser.query.filter_by(email=form.email.data).first()

        if user is None:
            flash('something wrong!')
            redirect(url_for('adminpage.login'))
        elif user.check_password(form.password.data):

            login_user(user)

            flash('Logged in successfully.')

            # login => admin page
            return redirect(url_for('adminpage.adminhome'))
        else:
            pass

    # ログインした状態でログインしないでいけるurlにはアクセスしようとしたらredirectする
    return  redirect(url_for('adminhome')) if current_user.is_authenticated else render_template('login.html', form=form)

@admin_blueprint.route('/signup', methods=['GET', 'POST'])
@login_required
def signup():
    form = SignupForm()

    if form.validate_on_submit():

        if AdminUser.query.filter_by(email=form.email.data).first():
            flash('Email has been registered already!')
            redirect(url_for('adminpage.signup'))


        elif AdminUser.query.filter_by(username=form.username.data).first():
            flash('Username has been registered already!')
            redirect(url_for('adminpage.signup'))

        else:
            user = AdminUser(email=form.email.data,
                            username=form.username.data,
                            password=form.password.data)

            db.session.add(user)
            db.session.commit()
            flash('Now You can login!')
            return redirect(url_for('adminpage.login'))
    return  render_template('signup.html', form=form)

# 一度adminhome行ったら、/adminかこのページかしかいけないようにすることが出来れば、
# 管理者と一般ユーザーのログイン状態を共有しているという致命的問題を間接的に解決したように見せかけられる
@admin_blueprint.route('/adminhome')
@login_required
def adminhome():

    return render_template('adminhome.html')