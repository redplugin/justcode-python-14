

SELECT * FROM products

----------------------
SELECT product_id FROM online_sales
EXCEPT
SELECT product_id FROM offline_sales


SELECT * FROM products
WHERE product_id IN (1, 3)
------------------------------------------

SELECT * FROM products
WHERE product_id IN (
	SELECT product_id FROM online_sales
	INTERSECT  -- EXCEPT, UNION
	SELECT product_id FROM offline_sales
)













