-- script that converts database to UTF8
-- convert the database
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- select database to use for this session of commands
USE hbtn_0c_0;
-- convert the table
ALTER TABLE first_table CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- convert the Field name in first_table
ALTER TABLE first_table CHANGE COLUMN name name varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
