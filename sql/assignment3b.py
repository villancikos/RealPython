import sqlite3

with sqlite3.connect('newnum.db') as connection:
	c = connection.cursor()

	while True:
		try:
			users_answer = int(raw_input("""What would you like to do (enter the number):
			1. AVG numbers in table.
			2. MAX number in table.
			3. MIN number in table.
			4. SUM of numbers in table.
			Enter any other number if you want to exit.
			"""))
			break
		except ValueError, e:
			print "exception", e.args[0]
	print users_answer
	if users_answer == 1:
		c.execute("SELECT AVG(num) FROM numbers")
		r = c.fetchone()
		print "AVG: "+ str(r[0])
	if users_answer == 2:
		c.execute("SELECT MAX(num) FROM numbers")
		r = c.fetchone()
		print "MAX: "+ str(r[0])
	if users_answer == 3:
		c.execute("SELECT MIN(num) FROM numbers")
		r = c.fetchone()
		print "MIN: "+ str(r[0])
	if users_answer == 4:
		c.execute("SELECT SUM(num) FROM numbers")
		r = c.fetchone()
		print "SUM: "+ str(r[0])
	else:
		exit()
