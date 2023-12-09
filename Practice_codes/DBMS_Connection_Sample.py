import pyodbc

# # Connect to the database using a DSN
# cnxn = pyodbc.connect("DSN=AUSU-TUF;UID=Login ID=?;PWD=Password=?")
#
# # Create a cursor
# cursor = cnxn.cursor()
#
# # Execute a query
# cursor.execute("SELECT * FROM mytable")
#
# # Fetch the results
# results = cursor.fetchall()
#
# # Iterate over the results and print each row
# for row in results:    print(row)
#
# # Close the cursor and connection
# cursor.close()
# cnxn.close()


# Connect to the database using a driver
cnxn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=my server;DATABASE=mydatabase;UID=myusername;PWD=mypassword")