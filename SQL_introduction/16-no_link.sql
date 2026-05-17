-- List all records of the table second_table with a name value
-- This script filters out rows with no name, displaying score and name ordered descending
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;

