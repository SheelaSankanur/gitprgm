create table customer(
	id int primary key,
    name varchar(50)
    );

create table orders(
	id int primary key,
    customer_id int,
    product varchar(50)
    );
insert into customer values(1,'sheela'),(2,'sakshi'),(3,'siddu');
insert into orders values(1,1,'laptop'),(2,1,'phone'),(3,2,'tablet');
-- show all customers with their orders use join
select customer.name,orders.product
from customer
inner join orders
on customer.id=orders.customer_id;

-- Show customers who placed orders only
select customer.name
from customer
inner join orders
on customer.id=orders.customer_id;

-- Show all customers even if no orders
SELECT customer.name, orders.product
FROM customer
LEFT JOIN orders
ON customer.id = orders.customer_id;

-- Show customers who did NOT place any order
select customer.name
from customer
left join orders
on customer.id=orders.customer_id
where orders.id is null;

-- Count how many orders each customer made
SELECT customer.name, COUNT(orders.id) AS total_orders
FROM customer
LEFT JOIN orders
ON customer.id = orders.customer_id
GROUP BY customer.name;

-- Show customer names with multiple orders
SELECT customer.name
FROM customer
JOIN orders
ON customer.id = orders.customer_id
GROUP BY customer.name
HAVING COUNT(orders.id) > 1;