use day1;
select *from students;
select*
from students
where age =(
	select age
	from students
	where name='Bob'
)
AND name!='Bob';

SELECT *
FROM students
WHERE age IN (
    SELECT age
    FROM students
    WHERE city = 'Bengaluru'
);

SELECT *from students
where age>(
select avg(age)
from students);

SELECT *
FROM students s
WHERE EXISTS (
    SELECT 1
    FROM enrollments e
    WHERE e.student_id = s.id
);

SELECT *
FROM students s
WHERE NOT EXISTS (
    SELECT 1
    FROM enrollments e
    WHERE e.student_id = s.id
);
