
-- Найти среднее значение столбца "revenue" для всех продаж из online_sales и offline_sales.

SELECT * FROM online_sales;

--------------------
SELECT 
	AVG(revenue) 
FROM offline_sales;
---------------------

SELECT product_id, sales_date, revenue FROM online_sales
UNION ALL
SELECT product_id, sales_date, revenue FROM offline_sales
--------------------

SELECT
	AVG(revenue)
FROM (
	SELECT revenue FROM online_sales
	UNION ALL
	SELECT revenue FROM offline_sales
);
----------------------

SELECT
	new_table.product_id,
	AVG(new_table.revenue)
FROM (
	SELECT product_id, revenue FROM online_sales
	UNION ALL
	SELECT product_id, revenue FROM offline_sales
) as new_table
GROUP BY new_table.product_id;

---------------------------
SELECT
	new_table.product_id,
	new_table.revenue
FROM (
	SELECT product_id, revenue FROM online_sales
	UNION ALL
	SELECT product_id, revenue FROM offline_sales
) as new_table
WHERE new_table.revenue > 100












































