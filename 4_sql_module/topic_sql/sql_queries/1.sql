SELECT * FROM users;


SELECT id, username, email 
FROM users
OFFSET 5
LIMIT 10;



SELECT *
FROM users
WHERE 
	id > 80 AND
	created_at > '2023-01-01 00:00:00';



SELECT * 
FROM users
WHERE email='andersonlori@example.org';

















