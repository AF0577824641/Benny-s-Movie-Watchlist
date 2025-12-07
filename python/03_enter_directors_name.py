import sqlite3

conn = sqlite3.connect("benny_movies.db")
cursor = conn.cursor()

# TODO: Input full name only functionality,

director_name = input("\nEnter director name: ")

# query database for movies by director
# Reference: (Will reference this later on for connecting the server mysql database) https://www.freecodecamp.org/news/connect-python-with-sql/
cursor.execute(
    """SELECT m.title, m.release_year
    FROM movies m
    JOIN director_to_movie dtm ON m.movie_id = dtm.movie_id
    JOIN directors d ON dtm.director_id = d.director_id
    WHERE d.full_name LIKE ?""",
    (f"%{director_name}%",),
)
movies = cursor.fetchall()

# BENNY (Code) 2025-11-30 :

if movies:
    print(f"\nFound {len(movies)} movies:")
    for movie in movies:
        print(f"- {movie[0]} ({movie[1]})")
else:
    print(
        "No movies found."
    )  # TODO: Add functionality to allow re-input if search doesn't exist instead of returning to main menu
conn.close()
