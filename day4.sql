use day1;
create table courses(
	id int auto_increment primary key,
	course_name varchar(50) not null
    );
INSERT INTO courses (course_name) VALUES
('Web Development'),
('Data Structures'),
('SQL Basics'),
('Advanced Python');

CREATE TABLE enrollments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
INSERT INTO enrollments (student_id, course_id) VALUES
(1, 1),  -- Alice → Web Development
(1, 2),  -- Alice → Data Structures
(2, 1),  -- Bob → Web Development
(3, 3),  -- Charlie → SQL Basics
(3, 4);  -- Charlie → Advanced Python
SELECT
    s.name AS student_name,
    c.course_name
FROM students s
INNER JOIN enrollments e ON s.id = e.student_id
INNER JOIN courses c ON e.course_id = c.id;