def get_tables(cursor):
    tables = []
    cursor.execute('SHOW TABLES')
    for table in cursor:
        tables.append(table[0])
    return tables