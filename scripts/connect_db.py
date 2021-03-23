import psycopg2 as db
from faker import Faker

conn_string = "dbname = 'dataengineering' host = 'localhost' user = 'postgres' password = '1991'"
conn = db.connect(conn_string)

cur = conn.cursor()

"""
Inserting data
Now that you have a connection open, you can insert data using SQL. To insert a single person,
you need to format a SQL insert statement, as shown:
"""

query = "insert into users (id,name,street,city,zip) values({},'{}','{}','{}','{}')".format(
    1, 'Big Bird', 'Sesame Street', 'Fakeville', '12345')
print(cur.mogrify(query))

"""
The preceding code will create a proper SQL insert statement;
however, as you progress, you will add multiple records in a single statement.
To do so, you will create a tuple of tuples. To create the same SQL statement, you can use the following code:
"""

query2 = "insert into users (id,name,street,city,zip) values(%s,%s,%s,%s,%s)"
data = (1, 'Big Bird', 'Sesame Street', 'Fakeville', '12345')
print(cur.mogrify(query2, data))
# cur.execute(query2, data)
# conn.commit()

fake = Faker()
data = []
i = 1002
for r in range(1000):
    data.append((i, fake.name(), fake.street_address(),
                 fake.city(), fake.zipcode()))
    i += 1


data_for_db = tuple(data)
print(cur.mogrify(query2, data_for_db[1]))
# cur.executemany(query2, data_for_db)
# conn.commit()
