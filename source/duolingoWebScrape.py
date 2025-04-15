from urllib import request
from bs4 import BeautifulSoup
import pandas as pd
import os

site = 'https://duolingodata.com' # this website contains the data (in table form) of Duolingo courses
html = request.urlopen(site) # Open the URL
soup = BeautifulSoup(html, 'html5lib') # Parse the HTML using html5lib as the html on the site is not well formatted

table = soup.find('table', {'id': 'DuolingoData'}) # Find the table with the specified ID

# Extract headers
headers = [th.get_text(strip=True) for th in table.find_all('th')] 

data = []
# Extracting the rows of the table
for row in table.find_all('tr'):
    cols = row.find_all('td') 
    if not cols:
        continue
    row_data = [col.get_text(strip=True) for col in cols]
    if len(row_data) == len(headers): # Check if the number of columns matches the headers
        data.append(row_data) # adds the data to the dataframe
    else:
        # reporting any mismatches
        print("Row skipped because of column mismatch", row_data)

df = pd.DataFrame(data, columns=headers)
# save the DataFrame to a CSV file which can be used for further analysis
# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the sibling 'data' folder
data_dir = os.path.join(current_dir, '..','data')


# Construct the full path for the CSV file
csv_path = os.path.join(data_dir, 'duolingo_data.csv')
df.to_csv(csv_path, index=False)