
SELECT DISTINCT products.* FROM offline_sales
LEFT JOIN products
ON products.product_id = offline_sales.product_id

-----------------------------------------

SELECT * FROM products
WHERE products.product_id IN (
	SELECT product_id FROM offline_sales
)

------------------------------------------

SELECT * FROM offline_sales
WHERE product_id=1;

SELECT 1 FROM offline_sales
WHERE product_id=1

---------------------------------------------

SELECT * FROM products
WHERE EXISTS (  -- NOT EXISTS
	SELECT 1 FROM offline_sales
	WHERE product_id = products.product_id
)

