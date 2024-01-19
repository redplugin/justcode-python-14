CREATE TABLE all_orders(
	order_id SERIAL PRIMARY KEY,
	user_id INTEGER, 
	product VARCHAR(30), 
	quantity INTEGER, 
	price NUMERIC(2)
);

ALTER TABLE all_orders
ADD created_at TIMESTAMP;


ALTER TABLE all_orders
ALTER product TYPE VARCHAR(50);


ALTER TABLE all_orders
DROP user_id;


ALTER TABLE all_orders
RENAME order_id TO id;

ALTER TABLE all_orders RENAME TO orders; 

SELECT * FROM orders;


