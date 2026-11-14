-- your query
Select department,name,salary,ranked from (SELECT *,DENSE_RANK() OVER(PARTITION BY department ORDER BY salary DESC) as ranked from employees) t where t.ranked<4;
