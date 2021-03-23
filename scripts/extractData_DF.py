import psycopg2 as db
import pandas as pd

conn_string = "dbname='dataengineering' host='localhost' user='postgres' password='1991'"
conn = db.connect(conn_string)

df = pd.read_sql("select * from users", conn)

df.to_json('data/dbtojson.json', orient='records')
