import random
import sqlite3
from random import randint

conn = sqlite3.connect("benny_movies.db")
cursor = conn.cursor()

# This connects to genre table and brings up all the movie

cursor.execute("SELECT * FROM genres")
all_genres = cursor.fetchall()  # MYSQL ref /  https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-fetchall.html

# randomly select a genre
random_genre = all_genres[randint(0, len(all_genres) - 1)]

# prints message of selected genre
print()  # return line empty
print(
    "Here's a random genre from Benny's collection:"
)  # Header print message once succesffuly randomized
print()  # return line empty
print(f"Title: {random_genre[1]}\nDescription: {random_genre[2]}")
conn.close()
