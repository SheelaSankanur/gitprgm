create table users(
	id int auto_increment primary key,
    name varchar(100) not null,
    email varchar(100) unique not null
    );
insert into users(name,email)values
('sheela','sheelasankanur06@gmail.com'),
('sakshi','sakshisankanur39@gmail.com'),
('bhavana','bhavanapolicpatel@gmail.com');
create table tasks(
	id int auto_increment primary key,
    title varchar(150)not null,
    description Text,
    status enum('pending','in_progress', 'completed') DEFAULT 'pending',
    user_id INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
INSERT INTO tasks (title, description, user_id) VALUES
('Learn MySQL Joins', 'Do Day 4 exercises', 1),
('Build API', 'Create REST API with Flask', 1),
('Review Code', 'Review frontend code', 2),
('Deploy App', 'Deploy to server', 3);
select*from users u where  exists(
select 1
from tasks t where t.user_id=u.id
);

SELECT *
FROM users u
WHERE NOT EXISTS (
    SELECT 1
    FROM tasks t
    WHERE t.user_id = u.id
);

SELECT *
FROM tasks
WHERE user_id IN (
    SELECT id
    FROM users
    WHERE name IN ('sheela', 'sakshi')
);
select 
	u.name,
	COUNT(t.id) as task_count
from users u left join tasks t on u.id=t.user_id 
group by
u.id,u.name;