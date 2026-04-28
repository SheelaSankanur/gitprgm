use day1;
alter table tasks
add column createdat datetime default current_timestamp;
select*from tasks;
SELECT CURRENT_TIMESTAMP AS now;
SELECT CURRENT_DATE AS today;
SELECT
    created_at,
    DATE(created_at) AS date_part,
    YEAR(created_at) AS year,
    MONTH(created_at) AS month,
    DAY(created_at) AS day
FROM tasks;