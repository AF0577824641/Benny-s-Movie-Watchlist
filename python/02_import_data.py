import csv
import sqlite3

# establish the 'cursor' needed to work inside the db
conn = sqlite3.connect("benny_movies.db")
cursor = conn.cursor()

# path to csv containing the data
data_genre = "genre.csv"
data_movie = "movies.csv"
data_directors = "directors.csv"
data_directorstomovie = "directors_to_movie.csv"
data_movie_genre = "movie_genre.csv"

# read in csv file and populate the database

# Import genres from CSV file
with open(data_genre, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader, None)  # skip the header row
    for row in csv_reader:
        # row[1] contains the genre name
        # insert into genres table, skip genre_id (auto-increments)
        cursor.execute(
            "INSERT OR IGNORE INTO genres (genre_name) VALUES (?)", (row[1],)
        )

# Import movies from CSV file
with open(data_movie, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader, None)  # skip the header row
    for row in csv_reader:
        # row[1] contains the movie title
        # insert into movies table, skip movie_id (auto-increments)
        cursor.execute("INSERT OR IGNORE INTO movies (title) VALUES (?)", (row[1],))

# Import directors from CSV file
with open(data_directors, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader, None)  # skip the header row
    for row in csv_reader:
        # row[1] contains the director name
        # insert into directors table, skip director_id (auto-increments)
        cursor.execute(
            "INSERT OR IGNORE INTO directors (director_name) VALUES (?)", (row[1],)
        )

# Import directors-to-movies relationships from CSV file
with open(data_directorstomovie, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader, None)  # skip the header row
    for row in csv_reader:
        # row[0] contains director_id, row[1] contains movie_id
        # insert the relationship between director and movie
        cursor.execute(
            "INSERT OR IGNORE INTO directors_to_movie (director_id, movie_id) VALUES (?, ?)",
            (row[0], row[1]),
        )

# Import movie-genre relationships from CSV file
with open(data_movie_genre, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader, None)  # skip the header row
    for row in csv_reader:
        # row[0] contains movie_id, row[1] contains genre_id
        # insert the relationship between movie and genre
        cursor.execute(
            "INSERT OR IGNORE INTO movie_genre (movie_id, genre_id) VALUES (?, ?)",
            (row[0], row[1]),
        )

print("All tables have been imported successfully")

# commit the command to the database
conn.commit()

# close the connection
conn.close()
