-- script that creates a table called first_table in the current datbase in
-- MySQL server, database name will be passed as argument of mysql command
-- without use of the SELECT or SHOW statements
CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
