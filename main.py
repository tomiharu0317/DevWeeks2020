from flask import render_template

from myproject import app

@app.route('/')
def index():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)

# QA
# ・直接指定のurlへとぶ方法
# ・アルゴリズム
# ・datetimeのdbへの渡し方