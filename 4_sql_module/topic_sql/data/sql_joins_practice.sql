SELECT * FROM orders;

SELECT * FROM order_details;

SELECT * FROM customers;

SELECT * FROM products;


-- 1
SELECT
	customers.customer_id,
	customers.company_name,
	orders.order_id,
	orders.employee_id,
	orders.order_date,
	orders.ship_city
FROM customers
INNER JOIN orders 
ON customers.customer_id = orders.customer_id
ORDER BY customers.customer_id
---------------------------------

-- 2
SELECT 
	products.product_name,
	categories.category_name
FROM products
LEFT JOIN categories
ON products.category_id=categories.category_id;
---------------------------------

-- 3 HW

-- 4
SELECT
	customers.company_name,
	orders.order_id,
	orders.order_date,
	orders.shipped_date,
	orders.ship_name,
	orders.ship_address
FROM customers
INNER JOIN orders 
ON customers.customer_id = orders.customer_id
WHERE orders.shipped_date IS NOT NULL
---------------------------------



-- 7
SELECT 
	categories.category_id,
	categories.category_name,
	SUM(order_details.unit_price * order_details.quantity) as total_sum
FROM products

LEFT JOIN order_details
	ON products.product_id = order_details.product_id

LEFT JOIN categories
	ON products.category_id = categories.category_id

GROUP BY categories.category_id, categories.category_name
--------------------------------------------------------
























