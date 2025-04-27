# Duolingo Data Analysis


## Overview
This project is a data analysis of the Duolingo language learning app. It uses web scraping and data management (through SQL and Python) to analyise the data. The data is then visualised in a blog written in Jupyter Notebook.

### Web Scraping

- The data was scraped from the website https://duolingodata.com using BeautifulSoup
- As the HTML on the website is poorly formatted, html5lib was used as the parser
- The output of the web scrape is a CSV file containing the following columns:
  - 'Learning': The language being learned
  - 'from': The language used to learn the new language (this is later referred to as 'Origin' to avoid conflict with the SQL keyword 'from')
  - 'U': The number of units in the course
  - 'Lr': The number of learners (millions)
  - 'Ls': The number of lessons in the course
  - 'S': The number of stories in the course
  - 'W': The number of words in the course
  - 'R': The release date of the course
  - 'D': The number of different lessons
- This file also created a new column 'CEFR' which contains the CEFR level of the course:
    - The initial web scrape included this within the 'Learning' column, but it was separated out for clarity, and because it is not always present
    - The seperation was done using regex

### Data Management

- The relationaldatabases.py file contains the code to read the CSV file, store its data in an SQLite database, and use relational databases to make the data more manageable. This file also contains the SQL queries which add a list of countries that speak the language to the database, which is used to create the map in the blog. 
- The database is a file called duolingoDatabase.db
- There is also a file named dataInvestigation.sql which contains some SQL queries to investigate the data in the database.

### Blog

- The blog is written in Jupyter Notebook and contains various visualisations of the data. 

## Running the Project

- To run the project, you will need Python 3.x and SQLite3 installed on your machine, along with the libraries imported in the code.
- The libraries used in the project are:
  - urllib
  - bs4
  - pandas
  - os
  - sqlite3
  - csv
  - matplotlib.pyplot
  - plotly.express
  - plotly.graph_objects
  - statsmodels.api
- The project is run in the following order:
  1. Run the web scraping code (duolingoWebScrape.py) to create the CSV file.
  2. Run the data management code (relationaldatabases.py) to create the SQLite database and add the data to it.
  3. Run the code in the Jupyer Notebook (blog.ipynb) to create the visualisations.
- Additionally, the queries in dataInvestigation.sql can be run to investigate the data in the database.

## Plots and Data
- The web scraping code and the data management code create files in the data folder. However, versions of these files are also included in the repository, but these will be overwritten if the code is run. 
- The plots produced in the blog are also included in the images folder, but these will be overwritten if the code is run to provide the most up to date versions.