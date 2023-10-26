from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

# Configuration for the PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://andrew.hagstrom:password@localhost/school_1'

# Initialize the SQLAlchemy extension
db = SQLAlchemy(app)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    subject = db.Column(db.String(1))

class Teachers(db.Model):
    # __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    subject = db.Column(db.String(1))

class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(1))

@app.route('/students', methods=['GET'])
def get_students():
    students = Students.query.all()
    print(students)
    print('^^^^raw sql quey results')

    #below is the sql command code
    raw_sql_query = """SELECT students.id, students.first_name, students.last_name, students.age, subjects.subject, teachers.first_name, teachers.last_name
FROM students INNER JOIN subjects 
ON students.subject = subjects.id
INNER JOIN teachers 
ON subjects.id = teachers.subject;"""

    #pass in the sql command code to execute and return the output to result
    result = db.session.execute(text(raw_sql_query))
    
    final_student_list = []

    # Each row is info for a student
    for row in result:
        print(row)
       output = {
    "id": row.id,
    "first_name": "Sophia",
    "last_name": "Wright",
    "age": 30,
    "class": {
      "subject": "Mathematics",
      "teacher": "David Miller"
    }
  },
  {
    // Next student data
  }
       
        # TODO: turn the row into a dict that matches the shape of the JSON we want to return
        # TODO: add that dict with the formatted student info into final_student list

    print(result)

    student_list = [
        {'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age, 'subject': student.subject} for student in students
    ]

    # TODO: replace student_list with final_student_list
    return jsonify(student_list)

@app.route('/teachers', methods=['GET'])
def get_teachers():
    teachers = Teachers.query.all()
    teacher_list = [
        {'id': teacher.id, 'first_name': teacher.first_name, 'last_name': teacher.last_name, 'age': teacher.age, 'subject': teacher.subject}
        for teacher in teachers
    ]

    return jsonify(teacher_list)

@app.route('/subjects', methods=['GET'])
def get_subjects():
    # __tablename__ = 'subjects'
    subjects = Subjects.query.all()
    subject_list = [
        {'id': subject.id, 'subject': subject.subject} for subject in subjects
    ]
    return jsonify(subject_list)

if __name__ == '__main__':
    app.run(debug=True)



