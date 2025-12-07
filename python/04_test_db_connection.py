# imports python libraries
# referenced colab (Shared Project 3): https://colab.research.google.com/drive/1YEqzHzwr1e8PFGz9xLvE9Xe9t742Nd_0?usp=sharing#scrollTo=2-bb-ddOBzjm
#
import sqlite3

# prints message upon running python sript
print("Welcome to Benny's Movie Watchlist Database\n")

running = True
while running:
    user_input = input("Press Enter to continue or Q to quit: ")
    # If user_input
    if user_input.lower() == "q":
        print("Goodbye! Thank you for using Benny's Movie Watchlist Database.")
        break
    # brings up the choice to
    choice = input(
        "\n0) About\n1) Search by Director\n2) Search by Genre\n3) Feeling Lucky For a Movie\n4) Feeling Lucky For a Genre\n5) Add New Movie\n6) Add Genre to Movie\n7) Add Director to Movie"
    )

    # connect to database
    conn = sqlite3.connect("benny_movies.db")
    cursor = conn.cursor()

    #  if choice == "0":
    #     import subprocess # TODO: add reference here

    #     subprocess.run(["python", ""])

    # Links to Enter Director Name python file
    if choice == "1":  # if user type in this number it will active the script
        import subprocess

        subprocess.run(["python", "03_enter_directors_name.py"])

    # Links to Enter Genre Name python file
    if choice == "2":
        import subprocess

        subprocess.run(["python", "03_enter_genre_name.py"])

    # Links to Random Movie python file
    if choice == "3":
        import subprocess

        subprocess.run(["python", "03_random_movie.py"])

    # Links to random genre python file

    if choice == "4":
        import subprocess

        subprocess.run(["python", "03_random_genre.py"])

    # Links to Input new movie python file
    if choice == "5":
        import subprocess

        subprocess.run(["python", "05_input_new_movie.py"])

    print()
