-- This SQL file is used to investigate the data in the database.
-- The database contains separate tables for each origin language, as well as a table for all data.
-- The tables are named according to the language they represent, such as EN for English, ES for Spanish, etc.
-- This file contains various queries to check the integrity and distribution of data.

-- Find the total number of learners that speak English
SELECT SUM(Lr) AS TotalOriginEnglish
FROM EN;
-- This is million at time of writing

-- Finding the total number of Spanish learners
SELECT SUM(Lr) AS TotalSpanishLearners
FROM all_data
WHERE Learning = 'Spanish';
-- this is 70.94 million at time of writing


-- Finding which languages offer courses in Guarani
SELECT DISTINCT origin_id
FROM all_data
WHERE learning LIKE 'Guarani';
