-- Lists all the records of the second table
SELECT score, name
FROM second_table
WHERE name != ''
ORDER BY score DESC;
