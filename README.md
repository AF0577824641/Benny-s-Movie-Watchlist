# Benny's Movie Watchlist

## Project Team

| Team Member        | Role & Responsibilities                                                                                                                                                         |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Shy Adelman**    | Data Visualization & Interface: Create visualizations (genre, decade, director), assist with randomizer logic, and help develop user interface components in Python             |
| **Adonis Fuentes** | Randomizers & Analysis Functions: Build global, genre, and decade randomizers; write analysis functions for films per decade and genre; support schema design and query testing |
| **Benny Candie**   | Data & Validation: Convert Word → TXT → CSV, clean and validate dataset, check duplicates, normalize director and genre labels, and verify all required fields                  |

**Integration:** All team members will collaborate to connect all elements, and the final product will be a running Python script with a UI in which we can search, find, rate, and update the database file based on user input.

## Project Overview

Benny's Movie Watchlist is an interactive, database-driven tool for exploring a curated selection of roughly 100–150 films. Inspired by Benny's personal collection of movies stored in a Word document, this project transforms a simple list into a structured database with querying, randomization, and visualization capabilities.

The project incorporates:

- Structured data modeling
- Data validation and transformation
- Python-based randomization features
- Visual exploration tools (optional, time permitting)

## Documentation

| Team Member        | Documentation Files                                                                                                                                                           |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Adonis Fuentes** | [Coding Notes](documentation/adonis_coding-notes.md) • [Responsibilities](documentation/adonis_responsibilities.md) • [Error Screen Recording](adonis_errors_screenrecording) |
| **Benny Candie**   | [Coding Notes](documentation/benny_coding-notes.md) • [Responsibilities](documentation/benny_responsibilities.md)                                                             |
| **Shy Adelman**    | [Coding Notes](documentation/shy_coding-notes.md) • [Responsibilities](documentation/shy_responsibilities.md)                                                                 |

## How it Works

### About the Database

Benny's Movie Database is a rudimentary and searchable movie database project conceived by Adonis Fuentes, Benny Candie, and Shy Adelman as a way to explore, practice, and implement python code in a practical and realistic way. This database is based off of Benny's Master Movie Watchlist (est. 2017), a personal, detailed list of over 1,000 movies that are ranked upon watch and organized alphabetically by director and genre. The goal of this project was to take that list and make it into a database using SQL and Python that could be edited, updated, and searched through via python on the backend while also allowing user-input and interaction on the front end. While rudimentary, the code as it stands acts as a proof of concept of the idea.

### How To Use

This database contains a selection of 150 movies from the watchlist. Users are able to use multiple choice options to receive a movie either at random or through searching via the multiple choice options provided. So far, the code allows for the user to "search" through the database for movies based on genre, director, or by randomization.

Users should be able to use multiple choice to be able to learn more about the project, restart to the beginning of the multiple choice options, or quit the interaction entirely.

# Libraries Used

- **[Random](https://docs.python.org/3/library/random.html)** - Random number generation and selection library
- **[SQLite3](https://docs.python.org/3/library/sqlite3.html)** - Lightweight database management library
- **[Pandas](https://pandas.pydata.org/)** - Data manipulation and analysis library
- **[Matplotlib](https://matplotlib.org/)** - Data visualization library

## Project Links

- **[Word Document](https://docs.google.com/document/d/1hvbzYHq9kyxoOdJOi9p1mjuIE28ZYHQcJG1S1CW_h68/edit?usp=sharing)** - Original movie watchlist
- **[Spreadsheet](https://docs.google.com/spreadsheets/d/1VJW1324CEw_mStu_CWv2US1oh3E22J63Zc-Ndmb2up8/edit?usp=sharing)** - Cleaned and structured data
- **[Proposal](https://docs.google.com/document/d/1iXk_IiontO1bKQAZjaLPTfbVtaJP0m8kGb_T8rcrT_U/edit?usp=sharing)** - Full project proposal
- **[Colab Workbook](https://colab.research.google.com/drive/1GtY7cb7FVBg8SbNqPq7MQbyjxgx50El-?usp=sharing)** - Project source code
- **[Presentation]()** -
