import psycopg2
def connect():
    try:
        """ Connect to the PostgreSQL database server """
        conn = psycopg2.connect(
            host="localhost",
            database="PyCoders",
            user="postgres",
            password="asd")

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        cur.execute("""
            CREATE TABLE Students(
                student_id serial PRIMARY KEY,
                name VARCHAR (50) UNIQUE NOT NULL
                );
            CREATE TABLE Teachers(
                teacher_id serial PRIMARY KEY,
                name VARCHAR (50) UNIQUE NOT NULL
                );
            INSERT INTO 
                Students(student_id,name)
            VALUES
                (1,'X'),(2,'Y'),(3,'Z');
            INSERT INTO 
                Teachers(teacher_id,name)
            VALUES
                (1,'A'),(2,'B'),(3,'C');
            SELECT * FROM Students
            UNION
            SELECT * FROM Teachers;
            ;
                """)

        # display the result of executed SQL query
        # you can also use fetchone() and fetchmany() according to your need
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