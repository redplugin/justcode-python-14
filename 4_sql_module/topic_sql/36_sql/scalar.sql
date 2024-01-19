-- Найти все продажи в online_sales где revenue выше
-- среднего (среднее значение по продажам онлайн).


SELECT AVG(revenue) FROM online_sales;

-- 99.2375


SELECT * FROM online_sales
WHERE revenue > 99.2375

----------------------

SELECT * FROM online_sales
WHERE revenue > (SELECT AVG(revenue) FROM online_sales)

-------------------

SELECT o.*
FROM online_sales as o,
	 (
	 	SELECT AVG(revenue) as avg_revenue FROM online_sales
	 ) as n

WHERE o.revenue > n.avg_revenue














