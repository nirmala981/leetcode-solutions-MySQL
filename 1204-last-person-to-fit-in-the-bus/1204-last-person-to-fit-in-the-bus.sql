# Write your MySQL query statement below
SELECT person_name
FROM Queue q
WHERE (
    SELECT SUM(q1.weight)
    FROM Queue q1
    WHERE q1.turn<=q.turn

)<=1000
order by q.turn DESC
LIMIT 1