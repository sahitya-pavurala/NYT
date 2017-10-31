SELECT
  customer_id,
  max(order_date)
  FROM orders
  GROUP BY customer_id;
