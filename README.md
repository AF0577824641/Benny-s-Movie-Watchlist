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

## Documentation

| Team Member        | Documentation Files                                    |
| ------------------ | ------------------------------------------------------ |
| **Adonis Fuentes** | [Documentation](documentation/adonis_documentation.md) |
| **Benny Candie**   | [Documentation](documentation/benny_documentation.md)  |
| **Shy Adelman**    | [Documentation](documentation/shy_documentation.md)    |

## How it Works

### About the Database

Benny's Movie Database is a rudimentary and searchable movie database project conceived by Adonis Fuentes, Benny Candie, and Shy Adelman as a way to explore, practice, and implement python code in a practical and realistic way. This database is based off of Benny's Master Movie Watchlist (est. 2017), a personal, detailed list of over 1,000 movies that are ranked upon watch and organized alphabetically by director and genre. The goal of this project was to take that list and make it into a database using SQL and Python that could be edited, updated, and searched through via python on the backend while also allowing user-input and interaction on the front end. While rudimentary, the code as it stands acts as a proof of concept of the idea.

### How To Use

This database contains a selection of 150 movies from the watchlist. Users are able to use multiple choice options to receive a movie either at random or through searching via the multiple choice options provided. So far, the code allows for the user to "search" through the database for movies based on genre, director, or by randomization.

Users should be able to use multiple choice to be able to learn more about the project, restart to the beginning of the multiple choice options, or quit the interaction entirely.

## Base Documentation

### Database Set Up

Data for the SQL database was set up using google sheets and all data was exported as a csv file. Data was lifted from the movie list manually and further expanded upon when necessary to help with the robustness of the data and to prevent unnecessary duplication in entries as a way to cut down on redundancy and make parsing through the database with code easier. Separate sheets were made for: Movies, Directors, and Genre and each entry in each data set was assigned a unique numerical ID (which would become necessary later when connecting the information to each other).

Additionally two sheets were made to map out the connections between movies and genres as well as directors to movies. In these sheets, should a movie occupy more than one genre (or a director more than one movie) their ID was associated w/ the corresponding ID of the movie or genre on a new line (if a director was associated with two movies, he would have two lines in the table, with one movie's ID associated with each line, rather than all of the IDs being associated with a single instance of the director's ID). This was done to maintain a 1:1 connection within the data between IDs while allowing us to associate multiple values to a single entity in a way that would be easily read and understood by the programming. These two connecting sheets (movies>directors and movie>genre) were used to connect the tables via SQL code.

### Server Set Up

In order to have the database accessible through something to demo (such as google colab) and to demonstrate an understanding of the backend of hosting such a project, the completed database was copied onto a server from freesqldatabase.com. This allows us to be able to host the information somewhere that can be easily found and connected to via python code. This allows us to pull the information from any computer rather than relying on only local files and connections and was done to help clean the code and parsing. An attempt was made to make a remote connection available via MySQL, but was unsuccessful due to the fact that it pissed me off and required too many IP permissions and specifications that frankly were not worth the effort. freesqldatabase was easier to set up and more seamless for the end result we had (to be able to demo this on google colab). This is on top of the fact that setting up the remote connection incorrectly via MySQL on your own computer can lead you to having an empty server totally open to the public web which is not only not safe or secure, but also stupid and can only be fixed by uninstalling the entirety of MySQL, downloading it again, and then retrying to start up a correct and secure remote connection. freesqldatabase takes on the brunt of all of that work so that is what is being used currently.

### Code Set Up

So, instead of creating individual files or one file with all of the code, we set it up so that the main Python script has subprocesses that are directed to the corresponding Python scripts for randomization, filtering, adding a new record, and searching for a director's name or a genre, and since the main file is also connected to the database, it keeps the code short and simple, and allows for a lot of modularity.

# Libraries Used

- **[Random](https://docs.python.org/3/library/random.html)** - Random number generation and selection library
- **[SQLite3](https://docs.python.org/3/library/sqlite3.html)** - Lightweight database management library
- **[Matplotlib](https://matplotlib.org/)** - Data visualization library

## Project Links

- **[Word Document](https://docs.google.com/document/d/1hvbzYHq9kyxoOdJOi9p1mjuIE28ZYHQcJG1S1CW_h68/edit?usp=sharing)** - Original movie watchlist
- **[Spreadsheet](https://docs.google.com/spreadsheets/d/1VJW1324CEw_mStu_CWv2US1oh3E22J63Zc-Ndmb2up8/edit?usp=sharing)** - Cleaned and structured data
- **[Proposal](https://docs.google.com/document/d/1iXk_IiontO1bKQAZjaLPTfbVtaJP0m8kGb_T8rcrT_U/edit?usp=sharing)** - Full project proposal
- **[Colab Workbook](https://drive.google.com/file/d/1kaxx_qDDpaWqphXpG3LHIhcZlJ6kbi-M/view?usp=sharing)** - Project source code
- **[Presentation](https://docs.google.com/presentation/d/1aDRs8g7IytimV2az55jIano7Z7z9rdrQjZ0RjT92Bjg/edit?usp=sharing)** (Group Final Presentation)-
