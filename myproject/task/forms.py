from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, RadioField, IntegerField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms.fields.html5 import DateField, TimeField


import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# 一ヶ月後まで登録可能
# 共通するもの
# ・毎～（保留）
# ・リマインドのラジオボタン
# 成績に占める割合

class FixedScheduleForm(FlaskForm):
    # タスクの名前
    # 時間（何日、何時から、何分間）

    taskname = StringField('Task Name', validators=[DataRequired()])
    # エスケープシーケンスだと思われているかも
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    startat = TimeField('Start Time', format='%H:%M', validators=[DataRequired()])
    endat = TimeField('End Time', format='%H:%M', validators=[DataRequired()])
    submit = SubmitField('Add')

class OtherWorksForm(FlaskForm):
    # タスクの名前
    # いつまで
    # 課題の重さ（重い、普通、軽い）

    taskname = StringField('Task Name', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    due = TimeField('Due', format='%H:%M', validators=[DataRequired()])
    taskweight = RadioField('課題の重さ', choices=[('3', '重い'), ('2', '普通'), ('1', '軽い')], validators=[DataRequired()])
    submit = SubmitField('Add')

class ReportForm(FlaskForm):
    # タスクの名前
    # いつまで
    # 内容の重さ（重い、普通、軽い）
    # 言語（日本語、英語、二外）
    # 文字数

    taskname = StringField('Task Name', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    due = TimeField('Due', format='%H:%M', validators=[DataRequired()])
    taskweight = RadioField('内容の重さ', choices=[('3', '重い'), ('2', '普通'), ('1', '軽い')], validators=[DataRequired()])
    lang = RadioField('レポートの言語', choices=[('3', '二外'), ('2', '英語'), ('1', '日本語')], validators=[DataRequired()])
    words = IntegerField('文字数', validators=[DataRequired()])
    submit = SubmitField('Add')


class TestForm(FlaskForm):
    # タスクの名前
    # いつまで
    # テスト時間
    # テストの重要度（重い、普通、軽い）

    taskname = StringField('Task Name', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    due = TimeField('Due', format='%H:%M', validators=[DataRequired()])
    test_time = IntegerField('テスト時間', validators=[DataRequired()])
    test_weight = RadioField('テストの重要度', choices=[('3', '重い'), ('2', '普通'), ('1', '軽い')], validators=[DataRequired()])
    submit = SubmitField('Add')

class TestPrepareForm(FlaskForm):
    # タスクの名前
    # いつまでに勉強するのか
    # テストの難易度

    taskname = StringField('Task Name', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    due = TimeField('Due', format='%H:%M', validators=[DataRequired()])
    test_weight = RadioField('テストの難易度', choices=[('3', '難しい'), ('2', '普通'), ('1', '簡単')], validators=[DataRequired()])
    submit = SubmitField('Add')

class PresentationForm(FlaskForm):
    # タスクの名前
    # いつまでに準備するのか
    # 発表時間
    # スライド枚数

    taskname = StringField('Task Name', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    due = TimeField('Due', format='%H:%M', validators=[DataRequired()])
    presentation_time = IntegerField('発表時間', validators=[DataRequired()])
    page_num = IntegerField('スライド枚数', validators=[DataRequired()])
    submit = SubmitField('Add')

class OndemandClassForm(FlaskForm):
    # タスクの名前
    # いつまで
    # 一回の視聴時間

    taskname = StringField('Task Name', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    due = TimeField('Due', format='%H:%M', validators=[DataRequired()])
    class_length = IntegerField('視聴時間', validators=[DataRequired()])
    submit = SubmitField('Add')

