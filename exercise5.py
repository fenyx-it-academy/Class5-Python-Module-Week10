import psycopg2

def connect():

    try:
        """ Connect to the PostgreSQL database server """
        conn = psycopg2.connect(
            host="localhost",
            database="PyCoders",
            user="postgres",
            password="Halo107.")

        # create a cursor
        cur = conn.cursor()

        #create a database
        # cur.execute("""
        #     CREATE TABLE students (
        #         student_id SERIAL PRIMARY KEY,
        #         name VARCHAR(255) NOT NULL
        #     );
        #     """)

        # cur.execute("""
        #     CREATE TABLE teachers (
        #         teacher_id SERIAL PRIMARY KEY,
        #         name VARCHAR(255) NOT NULL
        #     );
        #     """)

        # cur.execute("""
        #     INSERT INTO teachers (teacher_id,name)
        #     VALUES
        #     ('1','Halit'),
        #     ('2','Mehmet'),
        #     ('3','Samet');
        #     """)

        # cur.execute("""
        #     INSERT INTO students (student_id,name)
        #     VALUES
        #     ('1','Ahmet'),
        #     ('2','Selim'),
        #     ('3','Naim');
        #     """)

        cur.execute("""
            SELECT * from public."teachers";
            """)

        info = cur.fetchall()
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