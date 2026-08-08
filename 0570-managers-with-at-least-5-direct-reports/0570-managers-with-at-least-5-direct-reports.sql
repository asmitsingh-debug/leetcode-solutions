# Write your MySQL query statement below
select name from Employee where id in (select managerId from (select managerId,count(*) as num from Employee group by managerId having num>=5) t );