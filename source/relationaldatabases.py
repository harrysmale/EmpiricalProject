import sqlite3
import csv
import os

# Construct the database path based on current directory
base_dir = os.path.dirname(os.path.dirname(__file__))  # Go back one folder
db_path = os.path.join(base_dir, 'data', 'duolingoDatabase.db')
csv_path = os.path.join(base_dir, 'data', 'duolingo_data.csv')

# Delete the database file if it already exists
if os.path.exists(db_path):
    os.remove(db_path)

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create schemas
cursor.execute('''
CREATE TABLE IF NOT EXISTS origins (
    id INTEGER PRIMARY KEY,
    origin_name TEXT UNIQUE
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS all_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    learning TEXT,
    origin_id INTEGER,
    u INTEGER,
    lr REAL,
    ls INTEGER,
    s INTEGER,
    w INTEGER,
    r REAL,
    d INTEGER,
    cefr TEXT,
    FOREIGN KEY (origin_id) REFERENCES origins (id)
);
''')

# Collect all unique origins
origins = set() # Set is used to avoid duplicates
with open(csv_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        if len(row) >= 2 and row[1]: 
            origins.add(row[1])


# Sort origins alphabetically and assign IDs
sorted_origins = sorted(origins)
for idx, origin in enumerate(sorted_origins, 1):
    cursor.execute('INSERT INTO origins (id, origin_name) VALUES (?, ?)', (idx, origin))

# Inserting data into all_data table
with open(csv_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        if len(row) < 10:  # Skip rows with insufficient data
            continue
            
        learning, origin, u, lr, ls, s, w, r, d, cefr = row
        
        # Skip rows without origin
        if not origin:
            continue
            
        # Get origin_id
        cursor.execute('SELECT id FROM origins WHERE origin_name = ?', (origin,))
        result = cursor.fetchone()
        if not result:
            continue  # Skip if origin not found
            
        origin_id = result[0]
        
        # Insert data
        cursor.execute('''
        INSERT INTO all_data (learning, origin_id, u, lr, ls, s, w, r, d, cefr)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        ''', (learning, origin_id, u, lr, ls, s, w, r, d, cefr))

# Dropping rows with empty values in the Lr column - this is because in some cases there are duplicate courses for each language (such as an old and new version).
# The old version has no learners so it is not relevant to the analysis and should be dropped.
cursor.execute('''
               DELETE FROM all_data
               WHERE lr IS NULL OR lr = '';
               ''')

# Commit changes
conn.commit()

# Query the database to test the relational database
cursor.execute('SELECT id, origin_name FROM origins ORDER BY id')
print("Origins Table:")
for row in cursor.fetchall():
    print(row)

cursor.execute('''
SELECT a.id, a.learning, o.origin_name, a.u, a.lr, a.cefr 
FROM all_data a
JOIN origins o ON a.origin_id = o.id
LIMIT 10
''')


print("\nFirst 10 Rows:")
for row in cursor.fetchall():
    print(row)

# Close connection
conn.close()