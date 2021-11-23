import psycopg2

#connect to db
con=psycopg2.connect(
            host="localhost",
            database="PyCoders",
            user="postgres",
            password="Mndln.5516"
)

#cursor
cur=con.cursor()

#execute query
# cur.execute("CREATE TABLE students(student_id int PRIMARY KEY ,name text)")
# cur.execute("INSERT INTO students(student_id,name) VALUES(1234,'Ahmet')")
# cur.execute("INSERT INTO students(student_id,name) VALUES(1235,'Mehmet')")
# cur.execute("INSERT INTO students(student_id,name) VALUES(1236,'Yusuf')")
con.commit()

cur.execute("SELECT * FROM students")
for x in cur:
    print(x)



# cur.execute("CREATE TABLE teachers(teacher_id int PRIMARY KEY ,name text)")
# cur.execute("INSERT INTO teachers(teacher_id,name) VALUES(3456,'Ayse')")
# cur.execute("INSERT INTO teachers(teacher_id,name) VALUES(3457,'Nalan')")
# cur.execute("INSERT INTO teachers(teacher_id,name) VALUES(3458,'Kamil')")
con.commit()
cur.execute("SELECT * FROM teachers")
for x in cur:
    print(x)