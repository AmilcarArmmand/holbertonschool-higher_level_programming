-- MySQL script that creates the database hbtn_0d_2 and the user user_0d_2
-- create the database hbtn_0d_2 if it does not exist
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;
-- creates user user_0d_2 on server in localhost and sets password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- SELECT privileges granted
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
FLUSH PRIVILEGES;
