# shy vizualizer code

# NOTE: locally not sure why python lib section is not working, even though I did pip3 install matplotlib command and still get error: ModuleNotFoundError
import matplotlib.pyplot as plt
import numpy as np

# connect to database
conn = server_connection(
    "sql5.freesqldatabase.com", "sql5809971", "yrTE8cEQCi", "sql5809971"
)
cursor = conn.cursor()


# query the database to get genre counts
cursor.execute(
    "SELECT g.genre_name, COUNT(*) FROM genres g JOIN movie_genre mg ON g.genre_id = mg.genre_id GROUP BY g.genre_name"
)
genre_results = cursor.fetchall()

# extract data for the bar chart
genres = [row[0] for row in genre_results]
genre_counts = [row[1] for row in genre_results]

plt.figure(figsize=(10, 6))
x = np.array(genres)
y = np.array(genre_counts)

plt.bar(x, y, color="pink", width=0.1)

plt.title("Genre Breakdown from Benny's Movie Watchlist")
plt.xlabel("Genre")
plt.ylabel("Movies per genre ")
plt.show()

# close database connection
conn.close()

print("Pie chart created and saved as 'directors_gender.png'")
print("Bar chart created for genre breakdown")
