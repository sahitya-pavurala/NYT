SELECT
  a.customer_id,
  a.order_date,
  (a.quantity - b.quantity) as subtracted_quantity
  FROM  (SELECT o.customer_id, o.order_date, sum(o.quantity) as quantity
        FROM Orders o
        GROUP BY o.customer_id, o.order_date) a ,
        (SELECT o.customer_id, o.order_date, sum(o.quantity) as quantity
        FROM Orders o
        GROUP BY o.customer_id, o.order_date) b
        where a.customer_id = b.customer_id AND b.order_date < a.order_date AND a.quantity < b.quantity
        GROUP BY a.customer_id,a.order_date, a.quantity, subtracted_quantity ORDER BY a.customer_id asc;
