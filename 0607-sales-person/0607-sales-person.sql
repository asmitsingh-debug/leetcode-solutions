# Write your MySQL query statement below
SELECT s.name
FROM salesperson s
WHERE s.sales_id NOT IN (
    SELECT o.sales_id
    FROM orders o
    WHERE o.com_id = (
        SELECT com_id
        FROM company
        WHERE name = 'RED'
    )
);