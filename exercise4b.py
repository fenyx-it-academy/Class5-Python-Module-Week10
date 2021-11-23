import psycopg2

#connect to db
con=psycopg2.connect(
            host="localhost",
            database="Pagila",
            user="postgres",
            password="Mndln.5516"
)
#cursor
cur=con.cursor()

#execute query
cur.execute("select category_id,name,last_update from category")
rows=cur.fetchone()

for r in rows:
    print(r)

#close the cursor
cur.close()
#close to connection
con.close()