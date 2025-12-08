from connect_server import server_connection

# connect to database
conn = server_connection(
    "sql5.freesqldatabase.com", "sql5809971", "yrTE8cEQCi", "sql5809971"
)
cursor = conn.cursor()

genre_name = input("\nEnter genre name: ")

# query database for movies by genre
# reference: https://www.freecodecamp.org/news/connect-python-with-sql/
# reference: https://www.w3schools.com/python/python_mysql_select.asp
cursor.execute(
    """SELECT m.title, m.release_year
    FROM movies m
    JOIN movie_genre mg ON m.movie_id = mg.movie_id
    JOIN genres g ON mg.genre_id = g.genre_id
    WHERE g.genre_name LIKE %s""",
    (f"%{genre_name}%",),
)
movies = cursor.fetchall()

if movies:
    print(f"\nFound {len(movies)} movies:")
    for movie in movies:
        print(f"- {movie[0]} ({movie[1]})")
else:
    print("No movies found.")

conn.close()
