# Write your MySQL query statement below
WITH RankedScores AS (
    SELECT 
        student_id, 
        subject,

        FIRST_VALUE(score) OVER(PARTITION BY student_id, subject ORDER BY exam_date ASC) as first_score,

        FIRST_VALUE(score) OVER(PARTITION BY student_id, subject ORDER BY exam_date DESC) as latest_score,

        COUNT(exam_date) OVER(PARTITION BY student_id, subject) as attempt_count
    FROM Scores
)
SELECT DISTINCT 
    student_id, 
    subject, 
    first_score, 
    latest_score
FROM RankedScores
WHERE attempt_count >= 2 
  AND latest_score > first_score
ORDER BY student_id, subject;