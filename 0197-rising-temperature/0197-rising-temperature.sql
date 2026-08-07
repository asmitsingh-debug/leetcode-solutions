# Write your MySQL query statement below
select t.id from(select id,recordDate,temperature,lag(temperature) over(order by recordDate ) as temp_prv,
 lag(recordDate) over(order by recordDate ) as dt from Weather) t 
where t.temperature>t.temp_prv and DATEDIFF(t.recordDate, t.dt) = 1;