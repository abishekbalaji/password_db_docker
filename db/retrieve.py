import db.utils.connect as connect
from encoder_decoder import decoder
import db.utils.utils as utils
from db.utils.create_db import create_db

from tabulate import tabulate


cursor = connect.cursor
db_name = 'password_store'


def retrieve():
    # Create DB if it doesn't already exist
    create_db(db_name)
    cursor.execute(f'USE {db_name}')
    title = input("Enter the title: ")
    tables = utils.get_tables(cursor)
    if title not in tables:
        print(f"{title} not in {db_name}! Try adding it first.")
        return
    
    cursor.execute(f'SELECT * FROM {title}')

    data = cursor.fetchall()
    data_list = []
    for row in data:
        data_list.append([row[0], decoder(row[1])])
    print(tabulate(data_list, headers=['User Name', 'Password'], tablefmt='orgtbl'))