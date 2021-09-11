import sqlite3
def show_all():
	# Connect to database
	conn = sqlite3.connect('customer.db')
	# Create a cursor
	c = conn.cursor()
	# Query The Database and return all records
	c.execute("SELECT rowid, * FROM customers")
	items = c.fetchall()
	
	for item in items:
		print(item)
	
	# Commit Our Changes and Close The Connection
	conn.commit()
	conn.close()

























