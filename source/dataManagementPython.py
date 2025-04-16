import sqlite3
import csv
import os

# Construct the database path based on current directory (so it works for any user)
base_dir = os.path.dirname(os.path.dirname(__file__))  # Go back one folder
db_path = os.path.join(base_dir, 'data', 'duolingoDatabase.db')

# Delete the database file if it already exists
if os.path.exists(db_path):
    os.remove(db_path)

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the temp_data table
cursor.execute('''
CREATE TABLE IF NOT EXISTS temp_data (
    Leaning TEXT,
    Origin TEXT,
    U INTEGER,
    Lr REAL,
    Ls INTEGER,
    S INTEGER,
    W INTEGER,
    R REAL,
    D INTEGER
)
''')

csv_path = os.path.join(base_dir, 'data', 'duolingo_data.csv')


# Open the CSV file and insert its data into the temp_data table
with open(csv_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        cursor.execute('''
        INSERT INTO temp_data (Leaning, Origin, U, Lr, Ls, S, W, R, D)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', row)

# Get the unique values in the Origin column
cursor.execute("SELECT DISTINCT Origin FROM temp_data")
origins = cursor.fetchall()

# Dynamically create tables for each unique Origin value
for origin in origins:
    origin_value = origin[0]
    if origin_value:  # Skip empty Origin values
        create_table_schema_sql = f'''
        CREATE TABLE IF NOT EXISTS "{origin_value}" (
            Leaning TEXT,
            Origin TEXT,
            U INTEGER,
            Lr REAL,
            Ls INTEGER,
            S INTEGER,
            W INTEGER,
            R REAL,
            D INTEGER
        );
        '''
        cursor.execute(create_table_schema_sql)

        # Inserting data into new tables
        insert_data_sql = f'''
        INSERT INTO "{origin_value}" (Leaning, Origin, U, Lr, Ls, S, W, R, D)
        SELECT Leaning, Origin, U, Lr, Ls, S, W, R, D
        FROM temp_data
        WHERE Origin = "{origin_value}";
        '''
        cursor.execute(insert_data_sql)
        
# Commit the changes and delete the temp_data table
conn.commit()
cursor.execute("DROP TABLE temp_data")
conn.close()