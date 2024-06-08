import sqlite3

DB_PATH = "bank.db"


def create_table(sql_path: str):
    with open(sql_path, 'r') as sql:
        sql_query = sql.read()

    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.executescript(sql_query)

if __name__ == '__main__':
    create_table('create_bank.sql')


