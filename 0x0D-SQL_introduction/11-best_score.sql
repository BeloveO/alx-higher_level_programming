-- Lists all records with scores greater or equal to ten in the second table
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
