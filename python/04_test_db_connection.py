# imports python libraries
# Refrenced colab (Shared Project 3): https://colab.research.google.com/drive/1YEqzHzwr1e8PFGz9xLvE9Xe9t742Nd_0?usp=sharing#scrollTo=2-bb-ddOBzjm
#
import sqlite3

# prints message upon running python sript
print("Welcome to Benny's Movie Watchlist Database\n")

keep_going = True
while keep_going:
    user_input = input("Press Enter to continue or Q to quit: ")
    # If user_input
    if user_input == "Q" or user_input == "q":
        print("Goodbye! Thank you for using Benny's Movie Watchlist Database.")
        break
    # brings up the choice to
    choice = input(
        "\n1) Search by Director\n2) Search by Genre\n3) Feeling Lucky For a Movie\n4) Feeling Lucky For a Genre\nChoose 1 or 2: "
    )

    # connect to database
    conn = sqlite3.connect("benny_movies.db")
    cursor = conn.cursor()

    if choice == "1":
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

        if movies:
            print(f"\nFound {len(movies)} movies:")
            for movie in movies:
                print(f"- {movie[0]} ({movie[1]})")
        else:
            print(
                "No movies found."
            )  # TODO: Add functionality to allow re-input if search doesn't exist instead of returning to main menu

    elif choice == "2":
        genre_name = input("\nEnter genre name: ")

        # query database for movies by genre
        # Reference: https://www.freecodecamp.org/news/connect-python-with-sql/
        # Reference: https://www.w3schools.com/python/python_mysql_select.asp
        cursor.execute(
            """SELECT m.title, m.release_year
            FROM movies m
            JOIN movie_genre mg ON m.movie_id = mg.movie_id
            JOIN genres g ON mg.genre_id = g.genre_id
            WHERE g.genre_name LIKE ?""",
            (f"%{genre_name}%",),
        )
        movies = cursor.fetchall()

        if movies:
            print(f"\nFound {len(movies)} movies:")
            for movie in movies:
                print(f"- {movie[0]} ({movie[1]})")
        else:
            print(
                "No movies found."
            )  # prints no movies found inf user input movies that is not in the the db

    elif choice == "3":
        import subprocess

        subprocess.run(["python", "03_random_movie.py"])
    else:
        print("Invalid choice.")

    conn.close()
    print()
