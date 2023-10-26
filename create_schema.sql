DROP TABLE IF EXISTS students;
CREATE TABLE students (
  id           serial PRIMARY KEY,
  first_name   varchar(255) NOT NULL,
  last_name    varchar(255) NOT NULL,
  age          integer,
  subject      integer
);

COPY students FROM '/Users/andrew.hagstrom/Victor/day16/flask_postgres_school/data/student.csv' WITH 
(FORMAT CSV, HEADER true, DELIMITER ',');

DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
  id           serial PRIMARY KEY,
  first_name   varchar(255) NOT NULL,
  last_name    varchar(255) NOT NULL,
  age          integer,
  subject      integer
);

COPY teachers FROM '/Users/andrew.hagstrom/Victor/day16/flask_postgres_school/data/teachers.csv' WITH 
(FORMAT CSV, HEADER true, DELIMITER ',');

-- COPY your_table_name FROM '/path/to/your/file.csv' DELIMITER ',' CSV HEADER;

DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
  id           serial PRIMARY KEY,
  subject      varchar(255) NOT NULL
);

COPY subjects FROM '/Users/andrew.hagstrom/Victor/day16/flask_postgres_school/data/subjects.csv' WITH 
(FORMAT CSV, HEADER true, DELIMITER ',');


-- DROP TABLE IF EXISTS class;
-- CREATE TABLE class WHERE (FROM teachers INNER JOIN subjects ON teachers.subject  = subjects.id);



SELECT students.id, students.first_name, students.last_name, students.age, 
subjects.subject, teachers.first_name, teachers.last_name
FROM students INNER JOIN subjects 
ON students.subject = subjects.id

INNER JOIN teachers 
ON subjects.id = teachers.subject;

