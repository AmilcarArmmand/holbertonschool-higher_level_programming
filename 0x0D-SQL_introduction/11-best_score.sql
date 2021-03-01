-- script that lists all records of the table second_table of the database
-- MySQL server with a score >= 10 in order by score
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
