SELECT
    c.name AS customer_name,
    p.product_name AS product_name,
    p.category AS category,
    oi.quantity AS quantity,
    (oi.quantity * oi.item_price) AS total_spent,
    o.order_date AS order_date
FROM customers AS c
JOIN orders AS o ON o.customer_id = c.customer_id
JOIN order_items AS oi ON oi.order_id = o.order_id
JOIN products AS p ON p.product_id = oi.product_id
ORDER BY total_spent DESC
LIMIT 50;
