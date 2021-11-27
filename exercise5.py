import psycopg2

def connect():

    try:
        """ Connect to the PostgreSQL database server """
        conn = psycopg2.connect(
            host="localhost",
            database="Pycoders",
            user="postgres",
            password="****")
        
            
        # create a cursor
        cur = conn.cursor()
            
        # execute a statement
        cur.execute("""
            
            CREATE TABLE students(student_id serial PRIMARY KEY ,student_name VARCHAR (50) UNIQUE NOT NULL);
            CREATE TABLE teachers(teacher_id serial PRIMARY KEY ,teacher_name VARCHAR (50) UNIQUE NOT NULL)

            INSERT INTO Students(student_id,student_name) VALUES (1,'Xavi'),(2,'Yakup'),(3,'Zuleyha');
            INSERT INTO Teachers(teacher_id,teacher_name) VALUES (1,'Ali'),(2,'Yeliz'),(3,'Zeynep');

            SELECT * FROM Students 
            UNION
            SELECT * FROM Teachers;
            

            """)

        # display the result of executed SQL query
        info = cur.fetchall() # you can also use fetchone() and fetchmany() according to your need
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