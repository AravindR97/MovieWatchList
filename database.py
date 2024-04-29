import sqlite3

conn = sqlite3.connect()

with conn:
    conn.execute("CREATE TABLE IF NOT EXISTS movies (title TEXT, release_date REAL, watched INTEGER);")

