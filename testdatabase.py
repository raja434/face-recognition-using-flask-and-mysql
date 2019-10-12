import pymysql

# Open database connection
db = pymysql.connect("127.0.0.1","root","valaparla","face" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version 33: %s " % data)

# disconnect from server
db.close()