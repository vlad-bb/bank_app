import psycopg2
import sqlite3
from contextlib import contextmanager
from bank_table import DB_PATH


@contextmanager
def create_connection():
    try:
        """ create a database connection to database """
        conn = psycopg2.connect(host="localhost", database="test", user="postgres", password="123456")
        yield conn
        conn.close()
    except psycopg2.OperationalError as err:
        raise RuntimeError(f"Failed to create database connection {err}")
    
@contextmanager
def create_connection_sqllite():
    try:
        conn = sqlite3.connect(DB_PATH)
        yield conn
    except ConnectionError as err:
        print(err)
        conn.rollback()
    finally:
        conn.close()
