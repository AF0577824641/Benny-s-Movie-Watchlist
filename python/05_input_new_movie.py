import sqlite3

conn = sqlite3.connect("benny_movies.db")
eursor = conn.cursor()

# input fields for new movie
movie_title = input("Enter movie title: ")
movie_year = input("Enter movie year: ")
movie_description = input("Enter movie description: ")
movie_runtime = input("Enter running time (minutes): ")
movie_letterbox = input("Enter letterbox link: ")


# reference:https://stackoverflow.com/questions/35087508/mysql-not-able-to-execute-insert-into-table-column-count-doesnt-match-value

cursor.execute(
    "INSERT INTO movies (title, release_year, description, running_time, letterbox_link) VALUES (?, ?, ?, ?, ?)",
    (movie_title, movie_year, movie_description, movie_runtime, movie_letterbox),
)
movie_id = cursor.lastrowid

conn.commit()
print()
print(f"Your movie '{movie_title}' has been added to the database!")

conn.close()


# Todo List #
# TODO: updated print message to be more concise with details already input, and also after succesfull creationg make sure that input message is cleared since still shows up before print message.
# TODO: add error handling for invalid input
# TODO: link should be optional (Line13)
