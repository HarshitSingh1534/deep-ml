SELECT 
    o.order_id,
    SUM(xyz.quantity) AS units,
    SUM(xyz.order_price) AS items_total,
    SUM(xyz.order_price) + o.shipping_fee AS order_total
FROM (
    SELECT 
        oi.order_id AS order_id,
        oi.quantity AS quantity,
        oi.quantity * p.price AS order_price
    FROM order_items oi
    JOIN products p ON oi.product_id = p.product_id
) xyz
JOIN orders o ON xyz.order_id = o.order_id
GROUP BY o.order_id, o.shipping_fee;