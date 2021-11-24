import psycopg2

def connect():

    try:
        """ Connect to the PostgreSQL database server """
        conn = psycopg2.connect(
            host="localhost",
            database="Deneme",
            user="postgres",
            password="****")
            
        # create a cursor
        cur = conn.cursor()
            
        # execute a statement
        cur.execute(""" 
            SELECT * from public.actor;
            """)

        # display the result of executed SQL query
        info = cur.fetchall() # you can also use fetchone() and fetchmany() according to your need
        print(info)

        print("#####################################\n#####################################\n#####################################")

        cur.execute(""" 
            SELECT * from public.category ;
            """)

        info = cur.fetchone() # you can also use fetchone() and fetchmany() according to your need
        print(info)
        
        print("#####################################\n#####################################\n#####################################")

        cur.execute("""
            SELECT * from public.address ;
            """)

        info = cur.fetchmany(size=50) # you can also use fetchone() and fetchmany() according to your need
        print(info)

        # close the communication with the PostgreSQL
        cur.close()
        
        conn.commit()

    # catch the exception and print
    except (Exception) as error:
        print(error)

    finally:
        # close the connection at the end
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()
