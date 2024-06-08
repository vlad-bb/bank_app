import logging
from datetime import timedelta, datetime
from random import randint
from faker import Faker
from psycopg2 import DatabaseError
from connect import create_connection, create_connection_sqllite


fake = Faker('uk-Ua')
COUNT = 10

def insert_data_accounts(conn, sql_expression: str):
    c = conn.cursor()
    try:
        for _ in range(COUNT):
            created_at = fake.date()
            created_at_date = datetime.strptime(created_at, '%Y-%m-%d')
            updated_at = created_at_date + timedelta(days=randint(1, 3))
            c.execute(sql_expression, (fake.iban(), fake.currency_code(),
                      fake.pyfloat(left_digits=3, right_digits=2, positive=True),
                      created_at_date, updated_at))
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()

sql_insert_data_account = """
    INSERT INTO Accounts (iban, currency, balance, created_at, updated_at) VALUES (?, ?, ?, ?, ?);
    """

def main(func: callable, sql_expression):
    try:
        with create_connection_sqllite() as conn:
            if conn is not None:
                func(conn, sql_expression)
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)


if __name__ == "__main__":
    main(insert_data_accounts, sql_insert_data_account)