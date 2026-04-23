use day1;
select *from students;
create table courses(
	id int primary key,
    course_name varchar(100) not null
    );
insert into courses (course_name)values
('web'),
('data science'),
('sql'),
('python');
select *from courses;

create table enrollments(
	id int,
    student_id int,
    course_id int,
    foreign key(student_id) references students(id),
    foreign key(course_id) references courses(id)
    );
insert into enrollments(student_id,course_id)values
	(1,1),
    (1,2),
    (2,1),
    (3,3),
    (3,4);
select*from enrollments;
select s.name as student_name,c.course_name
from students s
inner join enrollments e on s.id=e.student_id
inner join courses c on e.course_id=c.id;

SELECT
    s.name AS student_name,
    c.course_name
FROM students s
LEFT JOIN enrollments e ON s.id = e.student_id
LEFT JOIN courses c ON e.course_id = c.id;
select s.name as student_name ,c.course_name
from students s
right join enrollments e on s.id =e.student_id
right JOIN courses c ON e.course_id = c.id;