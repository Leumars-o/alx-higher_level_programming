-- script that imports a table dump and displays the top 3 cities temp
-- during july and august ordered by temp
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
