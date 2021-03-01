-- script that creates a table second_table in the database in a MySQL server
-- database name will be passed as argument of mysql command
-- without using the SELECT and SHOW statements
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
INSERT INTO second_table (id, name, score)
VALUES (1, "John", 10),
       (2, "Alex", 3),
       (3, "Bob", 14),
       (4, "George", 8);
