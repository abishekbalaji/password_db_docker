import mysql.connector as mc

db = mc.connect(
    host='mysql-server',
    user='root',
    password='password'
)

cursor = db.cursor()
