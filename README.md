# Duolingo Data Analysis

## Web Scraping

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

## Data Management

- The dataManagementPython.py file contains the code to read the CSV file, store its data in an SQLite database, and then create separate tables for each unique 'Origin'. 