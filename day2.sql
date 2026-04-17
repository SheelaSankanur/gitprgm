use day1;
select*from students;
select*from students where age>=21 and age<=23;
select*from students where age between 21 and  23;
select*from students where city='bengaluru'or city='chennai';
SELECT * FROM students WHERE name LIKE 'A%';

select*from students order by age;
select *from students order by age desc;
SELECT * FROM students ORDER BY city, age;
select *from students limit 2;
select*from students order by age desc limit 2;
select*from students order by age limit 1,3;
select count(*) from students;
select count(*) from students where age>22;
select count(*) from students where city='bengaluru';
