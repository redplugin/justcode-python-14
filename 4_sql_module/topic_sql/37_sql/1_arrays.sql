
CREATE TABLE test(
	id SERIAL PRIMARY KEY,
	arr_column INTEGER[],
	arr_str_column VARCHAR[]
)


INSERT INTO test(arr_column, arr_str_column)
VALUES 
	('{1, 2, 4}', '{"test1", "test2"}')


SELECT * FROM test;




