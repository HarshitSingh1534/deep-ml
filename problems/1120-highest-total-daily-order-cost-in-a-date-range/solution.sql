-- your query
SELECT SUM(amount) from orders where order_date BETWEEN '2024-01-01' and '2024-01-31' group by 
customer_id,order_date order BY SUM(amount) desc LIMIT 1
