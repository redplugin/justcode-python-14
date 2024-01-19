
-- SELECT cast(group_id as INTEGER) FROM students
-- LIMIT 20;

-- SELECT group_id::INTEGER FROM students
-- LIMIT 20;

-- SELECT group_id, coalesce(group_id, 'Не состоит в группе')  FROM students
-- LIMIT 20;

SELECT *  FROM students
ORDER BY group_id NULLS FIRST;
