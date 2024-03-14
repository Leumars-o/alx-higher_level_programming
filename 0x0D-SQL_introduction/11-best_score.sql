-- Script that lists all records with a score >= 10 in second_table
SELECT name, score ORDER BY score
FROM second_table
WHERE score >= 10;
