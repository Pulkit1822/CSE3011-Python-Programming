import mysql. connector
conn = mysql.connector.connect(
host="127.8.8.1，
user="root", password="root",* database="vt"
With the help of execute ( one can run any MySQL
query
15
1〜
18
19
20
Showing list of tables
mycur=conn.cursor()
mycur.execute("show tables") for tb in mycur:
print(tb)
conn.close)