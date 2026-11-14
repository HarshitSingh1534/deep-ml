-- your query
SELECT * from (SELECT *,ROW_NUMBER() OVER(PARTITION BY department ORDER BY score DESC,employee) as rn, 
    RANK() OVER(PARTITION BY department ORDER BY score DESC) as rnk,
    DENSE_RANK() OVER(PARTITION BY department ORDER BY score DESC) as dense_rnk from scores) t ORDER BY t.department,t.score DESC,t.employee;
