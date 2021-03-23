import psycopg2 as db

conn_string = "dbname = 'dataengineering' host = 'localhost' user = 'postgres' password = '1991'"
conn = db.connect(conn_string)
cur = conn.cursor()

query = "select * from users"
cur.execute(query)

# for record in cur:
#     print(record)

# cur.fetchall()
# # where howmany equals the number of records you want returned
# cur.fetchmany(5)
# cur.fetchone()

# data = cur.fetchone()
# print(data[0])

# print(cur.rowcount)
# print(cur.fetchone())
# print(cur.rownumber)
# print(cur.fetchone())
# print(cur.rownumber)

with open('data/fromdb.csv', 'w') as f:
    cur.copy_to(f, 'users', sep=',')
