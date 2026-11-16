WITH dept_totals AS (
    SELECT 
        COALESCE((SELECT SUM(salary) FROM employees WHERE department = 'Sales'),0)       AS sales_total,
        COALESCE((SELECT SUM(salary) FROM employees WHERE department = 'Engineering'),0) AS engineering_total
)
SELECT 
    engineering_total,
    sales_total,
    engineering_total-sales_total AS salary_difference
FROM dept_totals;