# Write your MySQL query statement below
select x,y,z,
case
when x>0 and y>0 and z>0 and x + y > z
     AND x + z > y
     AND y + z > x then 'Yes'
else 'No'
end as triangle
from Triangle;