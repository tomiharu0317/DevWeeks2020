import os
from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from flask_admin import Admin, AdminIndexView

login_manager = LoginManager()

app = Flask(__name__, static_folder='static', template_folder='templates')

app.config['SECRET_KEY'] = 'mysecretkey'

basedir = os.path.abspath(os.path.dirname(__file__))

# Heroku Postgresアドオンを追加した場合、環境変数DATABASE_URLに
# PostgreSQLデータベースの接続先URLがセットされるので、この値が
# セットされているとき(Heroku上で動作するとき)はそれを使い、
# セットされていないとき(ローカルでのデバッグなど)はローカルのSQLiteデータベースを使うようにする。

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['FLASK_ADMIN_SWATCH'] = 'cosmo'

db = SQLAlchemy(app)
Migrate(app, db)

# 管理者画面の作成は凍結

# class MyAdminIndexView(AdminIndexView):
#     def is_accessible(self):
#         return current_user.is_authenticated

#     # rename auth.login
#     def inaccessible_callback(self, name, **kwargs):
#         return redirect(url_for('adminpage.login'))

# admin = Admin(app, template_mode='bootstrap3', index_view=MyAdminIndexView(),)

from myproject.auth.views import auth_blueprint
from myproject.task.views import task_blueprint
# from myproject.adminpage.views import admin_blueprint

app.register_blueprint(auth_blueprint, url_prefix='/authenticate')

# ログインしたときにユーザー名を持ってきて，prefixのusernameに入れる(とりあえず諦めた)
app.register_blueprint(task_blueprint, url_prefix='/user/')

# app.register_blueprint(admin_blueprint, url_prefix='/authenticate/admin')

login_manager.init_app(app)

# @login_requiredなのにログインせずアクセスしようとしたときにリダイレクトされる場所
# adminのログインの時にここにリダイレクトされてしまうので検討が必要

# この設定を無くすと、アクセスしようとしたときに401エラーを返す
login_manager.login_view = "auth.login"
# login_manager.login_view = "login"s
