-- Repeat buyers by completed orders
SELECT customer_id,
    COUNT(*) as completed_orders,
    SUM(amount) as total_spent 
    from orders where status='completed' group by customer_id having COUNT(*)>=2 AND SUM(amount)>=100;