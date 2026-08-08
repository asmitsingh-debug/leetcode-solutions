# Write your MySQL query statement below
with percte as (
    select customer_id,
    datediff(customer_pref_delivery_date,order_date)=0 AS immediate,
    dense_rank() over(partition by customer_id order by order_date) as first 
    from Delivery
) 
select  ROUND(AVG(immediate) * 100, 2) AS immediate_percentage
from percte where first=1;