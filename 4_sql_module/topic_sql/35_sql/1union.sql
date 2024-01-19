SELECT ons.product_id, ons.sales_date, ons.revenue FROM online_sales as ons;

SELECT offs.product_id, offs.sales_date, offs.revenue FROM offline_sales as offs;

---------------------------------

SELECT ons.product_id, ons.sales_date, ons.revenue FROM online_sales as ons
UNION
SELECT offs.product_id, offs.sales_date, offs.revenue FROM offline_sales as offs;

---------------

(SELECT ons.product_id, ons.sales_date, ons.revenue FROM online_sales as ons
LIMIT 1)

UNION

(SELECT offs.product_id, offs.sales_date, offs.revenue FROM offline_sales as offs
LIMIT 2);





