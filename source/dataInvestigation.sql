-- This SQL file is used to investigate the data in the database.
-- It contains various queries to check the integrity and distribution of data.

-- Find the total number of learners that speak English
SELECT SUM(Lr) AS TotalOriginEnglish
FROM EN;

