-- List to display average temperature by city
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY cities ORDER BY avg_temp DESC;
