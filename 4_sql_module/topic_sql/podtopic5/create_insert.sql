-- CREATE TABLE departments (
-- 	id 			SERIAL,
-- 	name		VARCHAR(30),
-- 	description TEXT,
	
-- 	PRIMARY KEY (id),
-- 	UNIQUE (name)
-- );

-- CREATE TABLE employees (
-- 	id 				SERIAL,
-- 	first_name		VARCHAR(30),
-- 	last_name		VARCHAR(30),
-- 	department_id 	INTEGER,
	
-- 	PRIMARY KEY (id)
-- );


-- INSERT INTO departments(name, description)
-- VALUES
-- 	('Отдел продаж', 'Занимается продажами'),
-- 	('Отдел разработки', 'Разрабатывают приложение'),
-- 	('Антифрод отдел', 'Пресекают возможные варианты мошенничества')

INSERT INTO employees (first_name, last_name, department_id)
VALUES
	('Макс', 'Фам1', 1),
	('Алекс', 'Фам2', 2),
	('Джон', 'Фам3', 3),
	('Дулат', 'Фам4', 4)
		

select * from departments;
select * from employees;