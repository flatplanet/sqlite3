import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Create a Table
c.execute("""CREATE TABLE customers (
		first_name text,
		last_name text,
		email text
	)""")

# Datatypes:
# NULL
# INTEGER
# REAL
# TEXT
# BLOB

# Commit our command
conn.commit()

# Close our connection
conn.close()




