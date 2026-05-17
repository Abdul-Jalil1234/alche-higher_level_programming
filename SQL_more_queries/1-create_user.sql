-- Create a MySQL server user with full privileges
-- This script provisions user_0d_1 on localhost with all access rights
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
