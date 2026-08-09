# Write your MySQL query statement below
with empcte as (
    select employee_id,department_id,
    row_number() over(partition by employee_id ORDER BY CASE
                WHEN primary_flag = 'Y' THEN 1
                ELSE 0
            END DESC
        ) AS num
    from Employee 
)
select employee_id,department_id from empcte where num=1;