-- CREATE TABLE test_table (
-- 	id			SERIAL PRIMARY KEY,
-- 	name		varchar(30) NOT NULL,
-- 	surname		varchar(30),
-- 	age			integer
-- );

-- * -> ALL 
SELECT * FROM test_table;

-- SELECT id as id_from_select, age FROM test_table;


-- INSERT INTO test_table (name, surname, age) VALUES ('justcode', 'python14', 15);


-- INSERT INTO test_table (surname, name, age) VALUES ('Kospan', 'Ulan', 18), ('Alex', 'Alex', 40);


-- INSERT INTO test_table (name) VALUES ('Alexandr'), ('Gabi');


INSERT INTO test_table (name, age) 
VALUES  ('Tengri', 65),
		('mklsdc', 65),
		('cdsc', 1);
		
		
		



SELECT * FROM test_table
WHERE surname is not NULL;














