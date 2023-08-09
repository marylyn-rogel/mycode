import sqlite3

conn = sqlite3.connect('my_database.db')

c = conn.cursor()

#creating the products table -- if it does not exist. there will be 4 columns
c.execute('''CREATE TABLE IF NOT EXISTS products
              (id INTEGER PRIMARY KEY,
               name TEXT,
               company_id INTEGER,
               FOREIGN KEY(company_id) REFERENCES companies(id))''')


 # Inserting data into the products table
c.execute("INSERT INTO products (id, name, company_id) VALUES (1, 'Widget', 4)")
c.execute("INSERT INTO products (id, name, company_id) VALUES (2, 'Gizmo', 2)")
c.execute("INSERT INTO products (id, name, company_id) VALUES (3, 'Thingamajig', 1)")
c.execute("INSERT INTO products (id, name, company_id) VALUES (4, 'Doohickey', 3)")
c.execute("INSERT INTO products (id, name, company_id) VALUES (5, 'Whatchamacallit', 6)")
c.execute("INSERT INTO products (id, name, company_id) VALUES (6, 'Gadget', 5)")

#saving changes
conn.commit()
conn.close()


