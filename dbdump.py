import sqlite3
from tabulate import tabulate

# Specify the path to your .db SQLite file
db_path = 'DM.db'

# Connect to the SQLite database
connection = sqlite3.connect(db_path)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Fetch the list of all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Loop through all tables and dump their contents
for table in tables:
    table_name = table[0]
    print(f"Dumping table: {table_name}")
    
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    
    # Fetch the column names
    column_names = [description[0] for description in cursor.description]
    
    # Print the table using tabulate for better formatting
    print(tabulate(rows, headers=column_names, tablefmt="grid"))
    print("\n")

# Close the connection
connection.close()
