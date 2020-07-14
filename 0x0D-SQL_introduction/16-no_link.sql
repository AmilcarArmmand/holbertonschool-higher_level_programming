-- script that lists all records in the table
-- second_table of the database MySQL server
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
