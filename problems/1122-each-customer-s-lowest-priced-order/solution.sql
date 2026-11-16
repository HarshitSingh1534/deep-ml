-- your query
SELECT order_id,customer_id,amount from (
    select *,ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY amount) as ranked from orders 
    ) where ranked=1;
