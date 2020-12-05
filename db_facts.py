import sqlite3
import random


CREATE_TABLE = '''CREATE TABLE IF NOT EXISTS facts (
                        id INTEGER PRIMARY KEY,
                        fact TEXT 
                )
               '''

INSERT = '''INSERT INTO facts (fact) VALUES (:fact) '''

DISPLAY = '''SELECT fact FROM facts WHERE id = (:id)'''

CLEAR_ALL = '''DELETE FROM facts'''


def connect():
    return sqlite3.connect("facts.db")


def create_table(connection):
    with connection:
        connection.execute(CREATE_TABLE)


def insert(connection, cursor, fact):
    with connection:
        cursor.execute(INSERT, {"fact": fact})


def display_fact(cursor):
    cursor.execute(DISPLAY, {"id": random.randint(0, 99)})
    fact = cursor.fetchall()
    return fact


def display_all(cursor):
    cursor.execute("SELECT * FROM FACTS")
    return cursor.fetchall()


def clear_all(connection, cursor):
    with connection:
        cursor.execute(CLEAR_ALL)
