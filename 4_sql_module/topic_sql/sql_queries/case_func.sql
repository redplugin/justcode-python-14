-- SELECT 
-- 	first_name as f4, 
-- 	group_id,
-- 	CASE
-- 		WHEN group_id='104' THEN 'Группа Сункар'
-- 		WHEN group_id='103' THEN 'Группа Скорая Помощь'
-- 		WHEN group_id='102' THEN group_id
-- 		ELSE 'Группа без названия'
-- 	END as group_name,
-- 	last_name
-- FROM students
-- LIMIT 20;





-- SELECT 
-- 	group_id, 
-- 	COUNT(id), 
-- 	COUNT(gender) FILTER (WHERE gender='Male') as Male,
-- 	COUNT(gender) FILTER (WHERE gender='Female') as Female,
-- 	COUNT(gender) FILTER (WHERE gender NOT IN ('Female', 'Male')) as Other
-- FROM students
-- GROUP BY group_id;





SELECT 
	group_id,
	COUNT(id),
-- 	ARRAY_AGG(first_name)
-- 	STRING_AGG(first_name, ' - ') FILTER (WHERE gender='Male') as MalesList,
-- 	STRING_AGG(first_name, ' - ') FILTER (WHERE gender='Female') as FemalesList
FROM students
GROUP BY group_id;



