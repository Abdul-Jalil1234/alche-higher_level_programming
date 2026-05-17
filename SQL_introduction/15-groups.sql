-- List the number of records with the same score in second_table
-- This script groups records by score, counting occurrences labeled as number, sorted descending
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;

