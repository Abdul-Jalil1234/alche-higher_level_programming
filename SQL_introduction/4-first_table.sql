-- Create a table called first_table in the current database
-- This script safely creates a table with an id and a name column
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
