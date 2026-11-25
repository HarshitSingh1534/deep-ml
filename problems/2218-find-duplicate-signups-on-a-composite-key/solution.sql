-- Duplicated (email, signup_date) keys
SELECT email,signup_date,COUNT(*) as copies,COUNT(*)-1 as extra_rows from signups group by signup_date,email having (COUNT(*)-1)>=1;