# ## 5. Create DB with Python

# - Create an empty database named `PyCoders` from your pgAdmin
# - Create a file named `exercise5.py`: this file will connect to `PyCoders` database
# - After connecting to database:
#   - Create a table with name `students`
#     - This table will have `student_id` and `name` columns
#   - Create a table with name `teachers`
#     - This table will have `teacher_id` and `name` columns
#   - Now add 3 records for both of these databases.
# - You should do all of these inside the python code. 
# - After doing these, run `SELECT` queries to get all data from both tables. Print these outputs.

import psycopg2

commands = (
        """
        CREATE TABLE students (
            student_id int PRIMARY KEY,
            name VARCHAR(50) NOT NULL
        )
        """,
           """
        CREATE TABLE teachers (
            teacher_id int PRIMARY KEY,
            name VARCHAR(50) NOT NULL
        )
        """,
        """insert into students(student_id,name) values (1,'Samet')
        """,
        """insert into students(student_id,name) values (2,'Osman')
        """,
        """insert into students(student_id,name) values (3,'Halit')
        """,
        """insert into teachers(teacher_id,name) values (1,'Irem')
        """,
        """insert into teachers(teacher_id,name) values (2,'Ceren')
        """,
        """insert into teachers(teacher_id,name) values (3,'Yavuz')
        """)
select_commands=("""
select * from students
""",
"""
select * from teachers
""")
try:
    conn = psycopg2.connect(database = "PyCoders",user = "postgres",host = "localhost",password = "1903")

    cur = conn.cursor()
    for command in commands:
        cur.execute(command)
    for command in select_commands:
        cur.execute(command)
        select=cur.fetchall()
        print(select)
    cur.close()
    conn.commit()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()