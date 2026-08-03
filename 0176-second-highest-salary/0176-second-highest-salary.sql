# Write your MySQL query statement below
with secondcte as(
    select salary,dense_rank() over(order by salary desc) as ranksal from Employee
)
select max(salary) as  SecondHighestSalary from secondcte where ranksal=2;