import sqlite3

# Query The DB and Return All Records
def show_all():
	# Connect to database and create cursor
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	
	# Query The Database
	c.execute("SELECT rowid, * FROM customers")
	items = c.fetchall()

	for item in items:
		print(item)

	# Commit our command and Close Connection
	conn.commit()
	conn.close()


# Add A New Record To The Table
def add_one(first,last,email):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))
	# Commit our command and Close Connection
	conn.commit()
	conn.close()

# Add Many Records To Table
def add_many(list):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
	# Commit our command and Close Connection
	conn.commit()
	conn.close()




# Delete Record from table
def delete_one(id):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.execute("DELETE from customers WHERE rowid = (?)", id)
	# Commit our command and Close Connection
	conn.commit()
	conn.close()

# Lookup with Where
def email_lookup(email):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.execute("SELECT rowid, * from customers WHERE email = (?)", (email,))
	items = c.fetchall()

	for item in items:
		print(item)

	# Commit our command and Close Connection
	conn.commit()
	conn.close()

