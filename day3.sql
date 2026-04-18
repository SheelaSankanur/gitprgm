use day1;
select name,upper(name) as name_upper,lower(name) as name_lower from students;
select name,substring(name,1,3)as name_prefix
from students;
select name ,LENGTH(name) as name_length from students;
select upper(name) as student_name,concat('age:',age) as info from students;
UPDATE students SET age = 25
WHERE name = 'BoB';
SELECT * FROM students WHERE name = 'Bob';
UPDATE students
SET city = 'Hyderabad'
WHERE name = 'BOB';