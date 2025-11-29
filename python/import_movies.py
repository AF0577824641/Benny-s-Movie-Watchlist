import csv
import sqlite3

# establish the 'cursor' needed to work inside the db
conn = sqlite3.connect("benny_movies.db")
cursor = conn.cursor()

# create path to csv containing the texts
data_file_path = "movies.csv"

# read in csv file and populate the database
with open(data_file_path, "r") as csv_obj:
    reader = csv.reader(csv_obj)
    next(reader, None)  # skips field names
    for row in reader:
        # insert text row by row, skip genre_id and let it auto-increment
        cursor.execute("INSERT OR IGNORE INTO movies (title) VALUES (?)", (row[1],))

print("process completed")

# commit the command to the database
conn.commit()

# close the connection
conn.close()
