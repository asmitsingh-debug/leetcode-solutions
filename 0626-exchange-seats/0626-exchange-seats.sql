# Write your MySQL query statement below
SELECT id, student
FROM (
    SELECT
        CASE
            WHEN id % 2 = 0 THEN id - 1
            WHEN id = (SELECT MAX(id) FROM Seat) THEN id
            ELSE id + 1
        END AS id,
        student
    FROM Seat
) t
ORDER BY id;