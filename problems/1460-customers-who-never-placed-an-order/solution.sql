-- your query
SELECT customer_id,name from customers where customer_id NOT IN (Select customer_id from orders where order_id is NOT NULL and customer_id is NOT NULL)