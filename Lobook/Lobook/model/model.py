# モジュール読み込み
import pymysql.cursors
# MySQLに接続する
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='sample',
                             charset='utf8',
                             # cursorclassを指定することで
                             # Select結果をtupleではなくdictionaryで受け取れる
                             cursorclass=pymysql.cursors.DictCursor)
# MySQLから切断する
connection.close()