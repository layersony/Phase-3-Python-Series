#!/home/layersony/.local/share/virtualenvs/phase-python-series-2WgKwfZU/bin/python
import sqlite3

class Students:
    # initialize variables
    def __init__(self, student_name, student_reg):
        self.student_name = student_name
        self.student_reg = student_reg

    def save(self, db_cursor, connection):
        db_cursor.execute(f'''INSERT INTO students (student_name, student_reg) 
                          VALUES ('{self.student_name}', '{self.student_reg}')''')
        connection.commit() # persist the changes

        print('Successfully added student')

    @classmethod
    def get_all_students(cls, db_cursor):
        return db_cursor.execute('SELECT * FROM students')

connection = sqlite3.connect('library.db')

db_cursor = connection.cursor() # 

### Create new Student

student1 = Students('Jane Doe', '20238765')
student1.save(db_cursor, connection)

student2 = Students('Jack Jill', '20231234')
student2.save(db_cursor, connection)

# print all students
all_students = Students.get_all_students(db_cursor)

for student in all_students:
    print(student)
db_cursor.close()
