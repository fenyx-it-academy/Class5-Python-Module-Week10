import psycopg2
import pandas as pd

conn = psycopg2.connect("dbname=PyCoders user=postgres password=12345")
cur = conn.cursor()

#cur.execute('INSERT INTO students VALUES(%s,%s)', (1,'firdevs'))
#cur.execute('INSERT INTO students VALUES(%s,%s)', (2,'jane'))
#cur.execute('INSERT INTO students VALUES(%s,%s)', (3,'jack'))
#cur.execute('INSERT INTO teachers VALUES(%s,%s)', (1,'ayşe'))
#cur.execute('INSERT INTO teachers VALUES(%s,%s)', (2,'ahmet'))
#cur.execute('INSERT INTO teachers VALUES(%s,%s)', (3,'rose'))

cur.execute("SELECT * FROM students")
rows = cur.fetchall()
df=pd.DataFrame(rows)
print(df)

cur.execute("SELECT * FROM teachers")
rows = cur.fetchall()
dg=pd.DataFrame(rows)
print(dg)


cur.close()
conn.commit()
conn.close()