# shy vizualizer code
import sqlite3
from typing import dataclass_transform

# NOTE: locally not sure why python lib section is not working, even though I did pip3 install matplotlib command and still get error: ModuleNotFoundError
import matplotlib as plt

conn = sqlite3.connect("benny_movies.db")
cursor = conn.cursor()

# query the database to get gender counts
cursor.execute("SELECT gender, COUNT(*) FROM directors GROUP BY gender")
results = cursor.fetchall()

# extract data for the pie chart
#
labels = []
sizes = []
for row in results:
    labels.append(row[0])
    sizes.append(row[1])

# Create the pie chart
plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",
    startangle=70,
    colors=["#8cb3d9", "thistle"],
)
plt.axis("equal")  # Ensures the pie chart is circular
plt.title("Gender of Directors from Benny's Movie Watchlist")  # Title of pie chart
plt.savefig("directors_gender.png", dpi=600)
plt.show()

# close database connection
conn.close()

print("Pie chart created and saved as 'directors_gender.png'")
