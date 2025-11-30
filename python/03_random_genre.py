Import random nynber
import sqlite3
from random import randint

# references:
# ref colab notebook:

# establish the 'cursor' needed to work inside the db
conn = sqlite3.connect("benny_movies.db")
cursor = conn.cursor()

# get all movies from the database
cursor.execute("SELECT * FROM movies")
all_movies = cursor.fetchall() # MYSQL ref /  https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-fetchall.html

# randomly select a movie
random_movie = all_movies[randint(0, len(all_movies) - 1)]

# Prints message of selected movie

print(f"Randomly selected movie: {random_movie}")
