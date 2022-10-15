import db.utils.connect as connect
from db.utils.create_db import create_db
from encoder_decoder import encoder
import db.utils.utils as utils

db = connect.db
cursor = connect.cursor


def get_data():
    title = input("Enter the title: ")
    no_of_entries = int(input("Number of entries: "))
    data = []
    for i in range(no_of_entries):
        user = input(f"User name for entry {i + 1}: ")
        password = input(f"Password for entry {i + 1}: ")
        encrypted_pass = encoder(password)
        data.append({'user': user, 'pass': encrypted_pass})
    return title, data


def store(db_name):
    # Create DB if it doesn't already exist
    create_db(db_name)
    title, data = get_data()
    cursor.execute(f'USE {db_name}')
    tables = utils.get_tables(cursor)
    if title not in tables:
        cursor.execute(f"CREATE TABLE {title} (user VARCHAR(255), pass VARCHAR(255))")
    else:
        print(f"\n{title} already exists in {db_name}\n")
    for row in data:
        val = (f"{row['user']}", f"{row['pass']}")
        print(val)
        sql = f"INSERT INTO {title} (user, pass) VALUES (%s, %s)"
        cursor.execute(sql, val)
        db.commit()
        print(cursor.rowcount, "record inserted.\n")
