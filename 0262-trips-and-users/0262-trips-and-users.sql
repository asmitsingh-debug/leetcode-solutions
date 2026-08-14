# Write your MySQL query statement below
select 
t.request_at AS Day,
    ROUND(SUM(IF(t.status LIKE 'cancelled%', 1, 0)) / COUNT(*), 2) AS `Cancellation Rate`
from Trips t join Users u1 on 
t.client_id=u1.users_id join users u2 on
t.driver_id=u2.users_id
where u1.banned='No' and u2.banned='No' 
AND t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
group by date(t.request_at);