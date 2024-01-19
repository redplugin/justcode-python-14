

SELECT product_id, COUNT(product_id)
FROM (
	SELECT product_id FROM offline_sales 
	UNION ALL
	SELECT product_id FROM online_sales 
)
GROUP BY product_id;

-----------------------------------
SELECT 
	*,
	(
		SELECT COUNT(product_id)
		FROM (
			SELECT product_id FROM offline_sales 
			UNION ALL
			SELECT product_id FROM online_sales 
		)
		GROUP BY product_id
		HAVING product_id = p.product_id
	)
FROM products as p

---------------------------------------------
-- TASK 2
SELECT * FROM online_sales
WHERE revenue > (
	SELECT AVG(revenue) FROM (
		SELECT revenue FROM online_sales
		UNION ALL
		SELECT revenue FROM offline_sales
	)
);















