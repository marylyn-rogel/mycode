import sqlite3


conn = sqlite3.connect('my_database.db')


#create a cursor object to execute SQL commands
c = conn.cursor()

#creating a table - if it does not exist! the table's name is "companies". it will have two columns.... one column is ID's. the other will be names.
c.execute('''CREATE TABLE IF NOT EXISTS companies
             (id INTEGER PRIMARY KEY,
              name TEXT)''')

c.execute("INSERT INTO companies (id, name) VALUES (1, 'Acme Inc.')")
c.execute("INSERT INTO companies (id, name) VALUES (2, 'XYZ Corp.')")
c.execute("INSERT INTO companies (id, name) VALUES (3, 'Apple Inc.')")
c.execute("INSERT INTO companies (id, name) VALUES (4, 'Samsung Electronics')")
c.execute("INSERT INTO companies (id, name) VALUES (5, 'Toyota Motor Corporation')")
c.execute("INSERT INTO companies (id, name) VALUES (6, 'Google LLC')")


#commit to save it! close it too
conn.commit()
conn.close()



