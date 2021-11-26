import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# user = "postgres"
# pwd = "1234"
# port = 5432
# host = "localhost"
# db_name = "pyCoders"
def create_database(db_name):
    try:
        conn = psycopg2.connect(port=5432, 
                                host="localhost", 
                                user="postgres", 
                                password="1234")

        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        # Create database
        cursor.execute("CREATE DATABASE {}".format(db_name))
        conn.close()



    except (Exception) as error:
        print(error)
    finally:
        # close the connection at the end
        conn.close()
        create_table(db_name)

def create_table(db_name):
    conn = psycopg2.connect(
            host="localhost",
            database=db_name,
            user="postgres",
            password="1234")

    cur = conn.cursor()
    
    cur.execute('''CREATE TABLE student
                    (student_id INT PRIMARY KEY NOT NULL,
                    name TEXT NOT NULL);''')
    
    cur.execute('''CREATE TABLE teacher
                    (teacher_id INT PRIMARY KEY NOT NULL,
                    name TEXT NOT NULL);''')
    id= [1,2,3]
    std=['Polat',"Mardona","Trump"]
    tchr=["Esra","Hakan","Ali"]
    for i in range(3):
        cur.execute(f"INSERT INTO student (student_id,name) \
                    VALUES ({id[i]}, '{std[i]}')")

        cur.execute(f"INSERT INTO teacher (teacher_id,name) \
                    VALUES ({id[i]}, '{tchr[i]}')")

    conn.commit()
    print("Records created successfully")
    conn.close()





if __name__ == '__main__':
    create_database("pycoders")





