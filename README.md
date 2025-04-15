# DUOLINGO Data Analysis

## Web Scraping

- The data was scraped from the website https://duolingodata.com using BeautifulSoup
- As the HTML on the website is poorly formatted, html5lib was used as the parser
- The output of the web scrape is a CSV file containing the following columns:
  - 'Learning': The language being learned
  - 'from': The language used to learn the new language
  - 'U': The number of units in the course
  - 'Lr': The number of learners (millions)
  - 'Ls': The number of lessons in the course
  - 'S': The number of stories in the course
  - 'W': The number of words in the course
  - 'R': The release date of the course
  - 'D': The number of different lessons

