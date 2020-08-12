from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Email,EqualTo

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# 一ヶ月後まで登録可能
# 共通するもの
# ・毎～（保留）
# ・リマインドのラジオボタン

class FixedScheduleForm(FlaskForm):
    # タスクの名前
    # 時間（何日、何時から、何分間）

    taskname = StringField('Name', validators=[DataRequired()])
    

    submit1 = SubmitField('予定')

class OtherWorksForm(FlaskForm):
    # タスクの名前
    # いつまで
    # 課題の重さ（重い、普通、軽い）

    submit2 = SubmitField('その他課題')

class ReportForm(FlaskForm):
    # タスクの名前
    # いつまで
    # 内容の重さ（重い、普通、軽い）
    # 言語（日本語、英語、二外）
    # 文字数

    submit3 = SubmitField('レポート')


class TestForm(FlaskForm):
    # タスクの名前
    # いつまで
    # テスト時間
    # テストの重要度（重い、普通、軽い）

    submit4 = SubmitField('テスト')

class TestPrepareForm(FlaskForm):
    # タスクの名前
    # いつまでに勉強するのか
    # テストの難易度

    submit5 = SubmitField('テスト対策')

class PresentationForm(FlaskForm):
    # タスクの名前
    # いつまでに準備するのか
    # 発表時間
    # スライド枚数

    submit6 = SubmitField('プレゼン')

class OndemandClassForm(FlaskForm):
    # タスクの名前
    # いつまで
    # 一回の視聴時間

    submit7 = SubmitField('授業')

