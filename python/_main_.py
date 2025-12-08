# imports python libraries
# referenced colab (Shared Project 3): https://colab.research.google.com/drive/1YEqzHzwr1e8PFGz9xLvE9Xe9t742Nd_0?usp=sharing#scrollTo=2-bb-ddOBzjm
#
import sqlite3
import subprocess

# prints message upon running python sript
print("Welcome to Benny's Movie Watchlist Database\n")

#
running = True
while running:
    # brings up the choice to
    choice = input(
        "\n0) About\n1) Search by Director\n2) Search by Genre\n3) Random Movie\n4) Random Genre\n5) Add New Movie\n\nEnter Q to quit: "
    )
    # If user_input
    if choice.lower() == "q":
        print("Goodbye! Thank you for using Benny's Movie Watchlist Database.")
        break

    # connect to database
    conn = sqlite3.connect("benny_movies.db")
    cursor = conn.cursor()

    if choice == "0":
        _ = subprocess.run(["python", "03_about.py"])

    # links to Enter Director Name python file
    if choice == "1":  # if user type in this number it will active the script
        _ = subprocess.run(["python", "03_enter_directors_name.py"])

    # links to Enter Genre Name python file
    if choice == "2":
        _ = subprocess.run(["python", "03_enter_genre_name.py"])

    # links to Random Movie python file
    if choice == "3":
        _ = subprocess.run(["python", "03_random_movie.py"])

    # links to random genre python file

    if choice == "4":
        _ = subprocess.run(["python", "03_random_genre.py"])

    # links to Input new movie python file
    if choice == "5":
        _ = subprocess.run(["python", "05_input_new_movie.py"])

    # links to piechart python file
    if choice == "8":
        _ = subprocess.run(["python", "06.1_piechart.py"])

    print()
