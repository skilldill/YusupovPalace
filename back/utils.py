import sqlite3

def get_cursor(db):
    conn = sqlite3.connect(db, check_same_thread=False)
    return conn.cursor()
