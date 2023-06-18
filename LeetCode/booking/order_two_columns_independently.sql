"""
Order Two Columns Independently


Table: Data

+-------------+------+
| Column Name | Type |
+-------------+------+
| first_col   | int  |
| second_col  | int  |
+-------------+------+
There is no primary key for this table and it may contain duplicates.

Write an SQL query to independently:

order first_col in ascending order.
order second_col in descending order.
The query result format is in the following example.
"""
# Write your MySQL query statement below

SELECT first_col, second_col
FROM (
    SELECT first_col, ROW_NUMBER() OVER(ORDER BY first_col ASC) AS r
    FROM Data
) a
JOIN (
    SELECT second_col, ROW_NUMBER() OVER(ORDER BY second_col DESC) AS r
    FROM Data
) b
ON a.r = b.r
