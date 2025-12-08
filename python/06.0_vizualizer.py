# shy vizualizer code

import sqlite3
from typing import dataclass_transform

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# read in our data and preview its contents
import pandas as pd

conn = sqlite3.connect("benny_movies.db")
cursor = conn.cursor()

# open file and see initial output

directors = pd.read_sql_query("SELECT * FROM directors", conn)
print(directors.head())

# visualize gender distribution

gender_counts = directors["gender"].value_counts()

print(gender_counts)

# close database connection
conn.close()
