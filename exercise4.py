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
cur.execute("select actor_id,first_name,last_name,last_update from actor")
rows=cur.fetchall()

for r in rows:
    print(r[0],r[1],r[2],r[3])

#close the cursor
cur.close()
#close to connection
con.close()