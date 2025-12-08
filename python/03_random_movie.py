import sqlite3
from random import randint

conn = sqlite3.connect("benny_movies.db")
cursor = conn.cursor()


cursor.execute("SELECT * FROM movies")
all_movies = cursor.fetchall()  # MYSQL ref /  https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-fetchall.html

# randomly selects a movie from database
random_movie = all_movies[randint(0, len(all_movies) - 1)]

# prints message of selected movie with proper formatting
print()  # return line empty
print(
    "Here's a random movie from Benny's collection:"  # Header print message once succesffuly randomized
)
print()  # return line empty
print(
    f"Title: {random_movie[1]}\nRelease Year: {random_movie[2]}\nDescription: {random_movie[3]}\nReview: {random_movie[4]}"
)
conn.close()

# TODO: Add option after randomization to let user choose to random will add option to after randomization has been execuated then give the option to suer if they want to keep on randomzinng again or go back to the main menu option, which also has print message for options. Also not sure if we want user to be able to input number of randomizations?
