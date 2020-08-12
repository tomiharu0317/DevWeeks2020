from werkzeug.security import generate_password_hash, check_password_hash
from flask_login  import UserMixin, current_user
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for
from datetime import datetime

from myproject import db, login_manager #, admin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# 一般ユーザーのデータベース
# 引数の順番がテーブルの順番と違うので余裕があれば揃える
class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)

# 管理者のデータベース
class AdminUser(db.Model, UserMixin):

    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)

タスクのデータベース
class Task(db.Model, UserMixin):

    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key = True)
    # 7種類のタスク分類があるので、ここをみて持ってくるcolumnを決める
    classification = db.Column(db.Integer, index=True)
    taskname = db.Column(db.String(128))
    date = db.Column(db.String(16))
    startat = db.Column(db.String(16))
    endat = db.Column(db.String(16))
    due = db.Column(db.String(16))
    taskweight = db.Column(db.Integer)
    lang = db.Column(db.Integer)
    words = db.Column(db.Integer)
    # anylength = (test_time, presentation_time, class_length)
    anylength = db.Column(db.Integer)
    page_num = db.Column(db.Integer)


# Customize Admin page Base view
class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))

# add a set of admin pages here.
# admin.add_view(MyModelView(User, db.session))
# admin.add_view(MyModelView(AdminUser, db.session))
# admin.add_view(MyModelView(Task, db.session))

