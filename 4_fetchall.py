import psycopg2

def connect():

    try:
        """ Connect to the PostgreSQL database server """
        conn = psycopg2.connect(
            host="localhost",
            database="pagila",
            user="postgres",
            password="1234")
            
        # create a cursor
        cur = conn.cursor()
            
        # execute a statement
        cur.execute("""
            SELECT * from "actor";
            """)
        # display the result of executed SQL query
        info = cur.fetchall() # Select all rows from actor table
        # info = cur.fetchmany(50)
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