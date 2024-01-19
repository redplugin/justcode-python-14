select * from departments;

select * from employees;

-- UPDATE employees
-- SET city='Astana', salary=89
-- WHERE id=16

INSERT INTO departments(id, name, description, city)
VALUES 
	(4, 'Отдел тестирования', 'QA отдел для тестировщиков', 'Semei')

-- INSERT INTO employees(first_name, last_name, department_id, city, salary)
-- VALUES 
-- 	('', '', 1, '', 150),
-- 	('Улан', 'Коспан', 2, 'Astana', 150),
-- 	('Амир', 'Фам6', 3, 'Aktobe', 150)



-- Task 1
SELECT 
	e.*,
	d.name,
	d.city as dep_city
FROM employees as e
INNER JOIN departments as d
ON e.department_id=d.id
WHERE e.city=d.city;
-----------------------------



-- Task 2
SELECT 
	e.*,
	d.name,
	d.city as dep_city,
	CASE
		WHEN e.city = d.city THEN 'Offline'
		WHEN e.city != d.city THEN 'Online'
	END as status
FROM employees as e
INNER JOIN departments as d
ON e.department_id=d.id;
-----------------------------


-- Task 3
SELECT
	departments.id as dep_id,
	departments.name,
	departments.city as dep_city,
	employees.first_name,
	employees.salary,
	employees.department_id 
FROM departments
LEFT JOIN employees
ON employees.department_id=departments.id
-- WHERE employees.* IS NULL;
-----------------------------


-- Task 4
SELECT 
	e.*,
	d.name,
	d.city as dep_city
FROM employees as e
INNER JOIN departments as d
ON e.department_id=d.id
ORDER BY e.salary DESC
LIMIT 5
-----------------------------


-- Task 5  -- Вложенная выборка ... [NOT] EXISTS
-----------------------------
























