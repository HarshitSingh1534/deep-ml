-- Units, items total and order total for each order
SELECT o.order_id,SUM(xyz.quantity) as units,SUM(xyz.order_price) as items_total,SUM(xyz.order_price)+o.shipping_fee as order_total from (
    SELECT oi.order_id as order_id,oi.quantity as quantity,oi.quantity*p.price as order_price from order_items oi JOIN products p ON oi.product_id=p.product_id) xyz 
JOIN orders o ON xyz.order_id=o.order_id group by o.order_id, o.shipping_fee