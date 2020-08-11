# Tips

## markdown記法

- [これ](https://qiita.com/tbpgr/items/989c6badefff69377da7)

## 開発の流れ

1. issueを見る
2. どのissueをやるかを報告
3. ブランチを切る
4. ブランチ内でコーディング
5. 見直す
6. コミット & プッシュ
7. マージされたら，masterブランチへ
8. masterを最新状態へ更新
9. 作業していたブランチを削除

```
git checkout -b feature/<作業名>#<issue番号>
git branch
git status
git add .
git commit -m "ここにやったことを書く"
git push origin feature/<作業名>#<issue番号>

PUll requestを送る

git checkout master
git pull
git branch --delete feature/<作業名>#<issue番号>
```

#### ブランチ内で作業しているときにmasterへ重要な変更があったとき

1. commitできそうなものはブランチ内でやっておく
2. masterへ
3. masterを最新に
4. 再び開発用ブランチへ
5. ブランチ内へmasterの内容を読み込む

```
(git add <コミットできそうなファイル>)
(git commit -m "メッセージ")
git checkout master
git pull origin master
git checkout feature/<作業名>#<issue番号>
git merge origin master
```

[参考](https://bake0937.hatenablog.com/entry/2017/11/07/081616)

## データベースの更新

```
---------------------------------------
MACOS/Linux
    $ export FLASK_APP=main.py
Windows
    $ set FLASK_APP=main.py

flask db init

# ここまでは最初だけ
----------------------------------------
flask db migrate -m "データベースの名前"
flask db upgrade
```

## ローカル環境で試す

```
python main.py
```

ブラウザで [http://127.0.0.1:5000/](http://127.0.0.1:5000/) にアクセス

## 今後やること

- ログイン後の画面
    - タスク一覧
        - タスクの追加
            - それぞれのタスクについて条件分岐
            - 毎週同じタスク
            - リマインド
        - タスクの完了
        - タスクの一覧
            - 表示件数の制限
            - 期限を過ぎたものは破棄
    - 今日のスケジュール
        - 活動時間こちら側でデフォルト，延ばす
        - タスクの重要度を決めるアルゴリズム
- 管理者画面
    - 管理者画面へのログイン
    - 内部のAdminIndexViewでのログアウト，メンバー追加