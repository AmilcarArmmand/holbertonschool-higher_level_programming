-- MySQL script that creates the table unique_id
-- with `id` INT with default value '1' and must be unique `name` varchar(256)
-- database name will be passed as an argument of the mysql command
CREATE TABLE IF NOT EXISTS unique_id(
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256) NOT NULL);
