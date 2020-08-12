from flask import render_template, redirect, url_for
from flask_login import current_user

from myproject import app

@app.route('/')
def index():

    # ログインした状態でログインしないでいけるurlにはアクセスしようとしたらredirectする
    return  redirect(url_for('task.scheduletoday')) if current_user.is_authenticated else render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)

# QA
# ・直接指定のurlへとぶ方法
# ・アルゴリズム
# ・datetimeのdbへの渡し方
# ・urlにusernameを渡す /<username>/scheduletoday

# 課題
# ・flashを消せるようにする/flashが表示される場所
# ・タスクの表示件数制限
# ・完成させる
# ・優先順位のアルゴリズム
# ・htmlファイルが多すぎるので構成を考え直すもしくはVue.jsなどを使ってSPA
# ・一般ユーザーと管理者のログイン管理状態を分離する
# ・最初にadmin用のsuperuserを作る方法（カスタムコマンドというのがある）

