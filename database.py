import datetime
import sqlite3

conn = sqlite3.connect("data.db")

# Create the table
with conn:
    conn.execute("""CREATE TABLE IF NOT EXISTS movies
    (title TEXT, release_timestamp REAL, watched INTEGER);""")

# Add a new movie to the table
def add_movie(title, timestamp):
    with conn:
        conn.execute("INSERT INTO movies VALUES (?, ?, 0)",(title, timestamp))

# Get the required form of table from the database
def get_movies(upcoming= False):
    if upcoming:
        timestamp_now = datetime.datetime.today().timestamp()
        return conn.execute("SELECT * FROM movies WHERE release_timestamp > ?;", (timestamp_now,))
    else:
        return conn.execute("SELECT * FROM movies;")

# Set watched status of movies to 1
def watch_movie(title):
    with conn:
        conn.execute("UPDATE movies SET watched = 1 WHERE title = ?", (title,))

# Get only the watched movies from the table
def get_watched_movies():
    return conn.execute("SELECT * FROM movies WHERE watched = 1;")
