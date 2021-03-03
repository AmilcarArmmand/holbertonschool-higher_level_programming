-- MySQL script that creates the database hbtn_0d_usa and the table cities
-- with `id` INT unique, auto generated, cannot be null and is a primary key
-- state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
-- with `name` varchar(256) cannot be null
-- if database or table name exists, script should not fail
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS cities(
       id INT UNIQUE PRIMARY KEY AUTO_INCREMENT NOT NULL,
       state_id INT NOT NULL,
       FOREIGN KEY (state_id) REFERENCES states(id),
       name VARCHAR(256) NOT NULL);
