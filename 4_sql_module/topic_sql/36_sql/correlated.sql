

SELECT * FROM online_sales;

SELECT * FROM products;

---------------------------

SELECT
	p.product_id,
	p.product_name,
	COUNT(o.*)
FROM products as p
LEFT JOIN online_sales as o
ON p.product_id = o.product_id
GROUP BY p.product_id

----------------------------

SELECT
	p.*,
	(
		SELECT 
			COUNT(*) 
		FROM online_sales as o
		WHERE o.product_id = p.product_id
	) as cnt
FROM products as p


















