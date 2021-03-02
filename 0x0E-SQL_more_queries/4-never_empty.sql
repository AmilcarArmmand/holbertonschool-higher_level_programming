-- MySQL script that creates the table id_not_null
-- with `id` INT with default value '1' and `name` varchar(256)
-- database name will be passed as an argument of the mysql command
CREATE TABLE IF NOT EXISTS id_not_null(
       id INT DEFAULT 1,
       name VARCHAR(256) NOT NULL);
