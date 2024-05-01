import datetime
import sqlite3

conn = sqlite3.connect("data.db")

# Create the table
with conn:
    # 'movies' table
    conn.execute("""CREATE TABLE IF NOT EXISTS movies
    (id INTEGER PRIMARY KEY, title TEXT, release_timestamp REAL);""")
    # 'users' table
    conn.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY);")
    # 'watched' table
    conn.execute("""CREATE TABLE IF NOT EXISTS watched
    (watcher TEXT, movie_id INTEGER, 
                FOREIGN KEY(watcher) REFERENCES users(username)
                FOREIGN KEY(movie_id) REFERENCES movies(id) );""")

# Add a new movie to the table
def add_movie(title, timestamp):
    with conn:
        conn.execute("INSERT INTO movies (title, release_timestamp) VALUES (?, ?)",(title, timestamp))

# Get the required form of table from the database
def get_movies(upcoming= False):
    if upcoming == True:
        timestamp_now = datetime.datetime.today().timestamp()
        return conn.execute("SELECT * FROM movies WHERE (release_timestamp > ?);", (timestamp_now,))
    else:
        return conn.execute("SELECT * FROM movies;")

# Move a movie to the watched table
def watch_movie(name,movie_id):
    with conn:
        conn.execute("INSERT INTO watched VALUES(?, ?);", (name, movie_id))

# Get only the watched movies from the table
def get_watched_movies(name):
    return conn.execute("""SELECT watched.watcher, movies.title FROM watched
                        JOIN movies ON watched.movie_id = movies.id
                        WHERE watcher = ?;""", (name,))

def add_user(name):
    with conn:
        conn.execute("INSERT INTO users VALUES (?);", (name,))

def close_connection():
    conn.close()
    print("\nConnection terminated.\n")