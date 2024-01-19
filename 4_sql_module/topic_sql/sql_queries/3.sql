CREATE TABLE test_table2 (
	id			SERIAL PRIMARY KEY,
	name		varchar(30) NOT NULL,
	age			integer CHECK (age > 10)
);


SELECT * FROM test_table2;

INSERT INTO test_table2(name, age)
VALUES ('amir', 9)