import sqlite3

# connects to the database
conn = sqlite3.connect("benny_movies.db")

# Create a cursor object to execute SQL queries on the database connection
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS directors (
  director_id INTEGER PRIMARY KEY AUTOINCREMENT,
  full_name VARCHAR(255) NOT NULL,
  birth_date DATE,
  death_date DATE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
  movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(255) NOT NULL,
  release_year SMALLINT,
  description TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS genres (
  genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
  genre_name VARCHAR(100) NOT NULL UNIQUE,
  genre_desc TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS director_to_movie (
  director_id INTEGER NOT NULL,
  movie_id INTEGER NOT NULL,
  PRIMARY KEY (director_id, movie_id),
  FOREIGN KEY (director_id) REFERENCES directors(director_id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (movie_id) REFERENCES movies(movie_id) ON DELETE CASCADE ON UPDATE CASCADE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS movie_genre (
  movie_id INTEGER NOT NULL,
  genre_id INTEGER NOT NULL,
  PRIMARY KEY (movie_id, genre_id),
  FOREIGN KEY (genre_id) REFERENCES genres(genre_id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (movie_id) REFERENCES movies(movie_id) ON DELETE CASCADE ON UPDATE CASCADE
)
""")

# commit the changes
conn.commit()

print("Tables created successfully!")

# close the connection when done
conn.close()
