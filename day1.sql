create database day1;
use day1;

create TABLE students(
    id int PRIMARY KEY,
    age int,
    name VARCHAR(50),
    city  varchar(50)
)
insert into students(id,age,name,city) values
(1,21,'sheela','guledgudd'),
(2,22,'sachin','badami');
SELECT *FROM students;
