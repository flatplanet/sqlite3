import sqlite3

# Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()



c.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@codemy.com')")





print("Command executed succesfully...")
# Commit our command
conn.commit()

# Close our connection
conn.close()




