-- Customers whose orders add up to at least 500
WITH totals AS (
    Select customer_id,sum(amount) as spent from orders group by customer_id) 
Select c.customer_id,c.name,s.spent from customers c join totals s on c.customer_id=s.customer_id where s.spent>=500;