import psycopg2
import pandas as pd


conn = psycopg2.connect("dbname=pagila user=postgres password=12345")
cur = conn.cursor()
#Select all rows from actor table
cur.execute("SELECT * FROM actor")
rows = cur.fetchall()
df=pd.DataFrame(rows)
print(df)

#Select first row of category table
cur.execute("SELECT * FROM category")
rows = cur.fetchmany(1)
df=pd.DataFrame(rows)
print(df)

#Select first 50 rows of address table
cur.execute("SELECT * FROM address")
rows = cur.fetchmany(50)
df=pd.DataFrame(rows)
print(df)


cur.close()
conn.commit()
conn.close()