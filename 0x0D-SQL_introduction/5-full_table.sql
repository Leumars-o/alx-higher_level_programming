-- Script that printts the full description
-- of the table from the database
SELECT column_name, data_type, character_maximum_length
FROM information_schema.columns
WHERE table_name = 'first_table';
