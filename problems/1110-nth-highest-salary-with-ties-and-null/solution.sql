-- your query
select salary from (SELECT *,DENSE_RANK() OVER(ORDER BY salary DESC) as nth_salary from employee) t where nth_salary=3 LIMIT 1;
