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
cur.execute("select address_id,address,address2,district,city_id,postal_code,phone,last_update from address")
rows=cur.fetchmany(50)

for r in rows:
    print(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7])

#close the cursor
cur.close()
#close to connection
con.close()