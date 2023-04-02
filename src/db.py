import sqlite3
from config import DB_FILEPATH

connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row

def get_db_connection():
    return connection

def drop_tables(conn):
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS users;")
    cur.execute('DROP TABLE IF EXISTS subjects;')
    cur.execute('DROP TABLE IF EXISTS questions;')

    conn.commit()

def create_tables(conn):
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE users (
        username TEXT UNIQUE,
        password TEXT 
    );''')

    cur.execute('''
    CREATE TABLE subjects (
        subject TEXT UNIQUE,
        username TEXT REFERENCES users
    )''')

    cur.execute('''
    CREATE TABLE questions (
        question TEXT UNIQUE,
        subject TEXT REFERENCES subjects,
        answer TEXT,
        q_type TEXT,
        username TEXT REFERENCES users
    )''')

    conn.commit()

def init_db():
    conn = get_db_connection()

    drop_tables(conn)
    create_tables(conn)

if __name__=='__main__':
    init_db()