LoBook-Django

#サーバー起動
python3 manage.py runserver

#アプリ作成
python3 manage.py startapp myapp
'myapp.apps.MyappConfig',
を追加
#DB セットアップ
python3 manage.py migrate

#DB定義

TABLE user

loginId:ログインID
password:パスワード

TABLE booklist

bookid: int
title:タイトル　char
auther:著者名 char
updatedAt:更新日時 date
createdAt:作成日時 date
purchaseDate:購入日 date
deadline:貸し出し期限 date
isAvailable:貸し出し状態 bool

TABLE review

bookid:
review: