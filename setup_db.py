import sqlite3

# Connect to the database. If it does not exist, it will be created.
conn = sqlite3.connect('my_database.db')

# Create a cursor object
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE accounts
             (name TEXT, account_type TEXT, balance REAL)''')

# Insert a row of data
cursor.execute("INSERT INTO accounts VALUES ('Sudeep','savings',1000.00)")
cursor.execute("INSERT INTO accounts VALUES ('Sushmita','savings',8888.00)")

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()
