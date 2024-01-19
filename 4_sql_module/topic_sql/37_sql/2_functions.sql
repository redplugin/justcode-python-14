SELECT * FROM products;
--------

---- STRING
SELECT category, LENGTH(category) FROM products;
-----
SELECT category, UPPER(category), LOWER(category) FROM products;
-----
SELECT *, CONCAT(product_name, ' + ', category) FROM products;
-----
SELECT *, SUBSTRING(category FROM 2 FOR 3) FROM products;



----------------------------------------------------
SELECT ABS(-15);
----
SELECT revenue, ROUND(revenue, 0) FROM online_sales;
----
SELECT revenue, CEIL(revenue) FROM online_sales;
----
SELECT revenue, FLOOR(revenue) FROM online_sales;

----------------------------------------------------



SELECT NOW();
----
-- SELECT EXTRACT('DOY' FROM NOW());
-- datetime.weekday()  [0-6] 0 - monday
-- DOW  [0-6] 0 - sunday

-- SELECT EXTRACT('YEAR' FROM TIMESTAMP '2024-01-07');
SELECT EXTRACT('DOW' FROM TIMESTAMP '2024-01-07');

------------------------------------------

-- SELECT DATE_TRUNC('CENTURY', TIMESTAMP '2024-05-14 12:34:37');
SELECT DATE_TRUNC('MONTH', TIMESTAMP '2024-05-14 12:34:37');


----------------------------


SELECT SQRT(25);

SELECT *, SQRT(revenue) FROM online_sales;
----

SELECT POWER(5, 3);
SELECT *, POWER(revenue, 0.5) FROM online_sales;
----

SELECT LOG(2, 8);

-----------------------

-- SELECT revenue, CAST(revenue AS INTEGER) FROM online_sales;
SELECT revenue, revenue::INTEGER FROM online_sales;

----------------

SELECT
	product_id,
	sales_date,
	revenue
FROM online_sales
ORDER BY revenue;
---------

SELECT
	product_id,
	sales_date,
	revenue,
	ROW_NUMBER() OVER (ORDER BY revenue DESC)
FROM online_sales;
-------


SELECT
	product_id,
	sales_date,
	revenue,
	ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY sales_date) as res
FROM online_sales;



---------------------
SELECT
	product_id,
	SUM(revenue),
	ROW_NUMBER() OVER (ORDER BY SUM(revenue) DESC) as res
FROM online_sales
GROUP BY product_id
---------------------
SELECT
	product_id,
	SUM(revenue),
	RANK() OVER (ORDER BY SUM(revenue) DESC) as res
FROM online_sales
GROUP BY product_id
----------------------

SELECT
	product_id,
	SUM(revenue),
	DENSE_RANK() OVER (ORDER BY SUM(revenue) DESC) as res
FROM online_sales
GROUP BY product_id
----------------------





SELECT
	product_id,
	sales_date,
	ROW_NUMBER() OVER (ORDER BY sales_date) as res
FROM online_sales;


SELECT
	product_id,
	sales_date,
	RANK() OVER (ORDER BY sales_date) as res
FROM online_sales;


SELECT
	product_id,
	sales_date,
	DENSE_RANK() OVER (ORDER BY sales_date) as res
FROM online_sales;


