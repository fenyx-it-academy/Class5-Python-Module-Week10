# ## 4. Connect to DB with Python

# - Now, connect to this imported Pagila database from python code.
# - Select all rows from `actor` table
# - Select first row of `category` table
# - Select first 50 rows of `address` table

# Do the above operations inside python code. (Use `fetchOne()`, `fetchMany()`, `fetchAll()` etc.) 

import psycopg2

commands = (
        """
    select * from actor
        """)

commands1 = (
        """
    select * from category limit 1
        """)
commands3 = (
        """
    select * from adress limit 50
        """)
try:
    conn = psycopg2.connect(database = "exercise3",user = "postgres",host = "localhost",password = "1903")
    cur = conn.cursor()
    print("All rows of actor")
    cur.execute(commands)
    select=cur.fetchall()
    for i in select:
        print(i) #all rows of actor 

    
    cur.execute(commands1)
    first_row_category=cur.fetchone()#First row of category
    print("### First Row of Category table")
    print(first_row_category)

    print('First 50 rows of adress')
    cur.execute(commands)
    first_50_rows=cur.fetchmany(50)
    for i in first_50_rows:
        print(i) #first 50 rows of adress 
    
    cur.close()
    conn.commit()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()