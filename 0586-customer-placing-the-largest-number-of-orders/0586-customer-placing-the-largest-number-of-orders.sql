# Write your MySQL query statement below
with regular as
(select customer_number,count(*) as total from orders group by customer_number)
select customer_number from regular where total=(select max(total) from regular);