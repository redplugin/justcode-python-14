SELECT ons.product_id, ons.sales_date, ons.revenue FROM online_sales as ons;

SELECT offs.product_id, offs.sales_date, offs.revenue FROM offline_sales as offs;

---------------------------------

SELECT ons.product_id, ons.sales_date, ons.revenue, 'Online' as status FROM online_sales as ons
UNION
SELECT offs.product_id, offs.sales_date, offs.revenue, 'Offline' FROM offline_sales as offs;

---------------


-- SELECT ons.order_id, 'test' from online_sales as ons;


