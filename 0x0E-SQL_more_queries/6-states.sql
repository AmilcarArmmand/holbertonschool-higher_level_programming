-- MySQL script that creates the database hbtn_0d_usa and the table states
-- with `id` INT unique, auto generated, cannot be null and is a primary key
-- with `name` varchar(256) cannot be null
-- if database or table name exists, script should not fail
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS states(
       id INT UNIQUE PRIMARY KEY AUTO_INCREMENT NOT NULL,
       name VARCHAR(256) NOT NULL);
