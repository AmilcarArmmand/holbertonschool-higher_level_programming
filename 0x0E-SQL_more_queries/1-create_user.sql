-- MySQL script that creates user user_0d_1 with all privileges
-- creates user user_0d_1 on server in localhost and sets password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- all privileges granted
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
