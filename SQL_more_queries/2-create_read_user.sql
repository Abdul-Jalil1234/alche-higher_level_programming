-- Create the database hbtn_0d_2 and the user user_0d_2
-- This script provisions the database and sets up a read-only user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create the user user_0d_2 if it does not already exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant only SELECT privileges on the hbtn_0d_2 database to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

