SELECT ons.product_id, ons.sales_date, ons.revenue FROM online_sales as ons;

SELECT offs.product_id, offs.sales_date, offs.revenue FROM offline_sales as offs;

---------------------------------

SELECT ons.product_id FROM online_sales as ons
INTERSECT
SELECT offs.product_id FROM offline_sales as offs;

---------------

(SELECT ons.product_id FROM online_sales as ons
LIMIT 2)

INTERSECT

(SELECT offs.product_id FROM offline_sales as offs
LIMIT 2);





