import psycopg2


def connect():
    try:
        ' Connect to the PostgreSQL database server '
        conn = psycopg2.connect(
            host='localhost',
            database='PyCoders',
            user='postgres',
            password='1')

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        cur.execute("""
                create table students(
                    student_id integer,
                    name varchar(50)
                ) ;
                create table teachers(
                    teacher_id integer,
                    name varchar(50)
                ) ;
                INSERT INTO students(student_id,name)
                VALUES (1,'ali'),(2,'veli'),(3,'memet');

                INSERT INTO teachers(teacher_id,name) 
                VALUES (1,'ayse'), (2,'fatma'),(3,'huseyin')
                ;
                select * from public.students
                union
                select * from public.teachers; 
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
