-- script that lists all records of the table second_table of the database
-- MySQL server, results will display the score and name in order by score
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
