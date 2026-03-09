use teachers;
create table teachers(
	teacher_ID INT,
    teacher_name VARCHAR(50),
	teacher_age INT
);
insert into teachers(
    teacher_ID,
    teacher_name,
    teacher_age
)
values
(253,'sheela',25),
(254,'sakshi',26);

select * from teachers;
