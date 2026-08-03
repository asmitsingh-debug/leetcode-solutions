# Write your MySQL query statement below
with topthreecte as(
    select Department.name as Department,Employee.name as Employee,Employee.salary as Salary,
    dense_rank() over(partition by Department.name order by Employee.salary desc) as rnk from Employee join Department on Employee.departmentId=Department.id 
)
select Department,Employee, Salary from topthreecte where rnk=1;