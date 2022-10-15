import db.utils.connect as connect

cursor = connect.cursor

# List databases
cursor.execute('SHOW databases')

db_list = []
for db in cursor:
    db_list.append(db[0])


def create_db(db_name):
    if db_name not in db_list:
        cursor.execute(f'CREATE DATABASE {db_name}')
        if cursor:
            print(f"DB {db_name} created successfully.")
    else:
        print(f"{db_name} already exists!")