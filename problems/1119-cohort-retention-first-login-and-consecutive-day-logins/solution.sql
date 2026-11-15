-- your query
SELECT user_id,MIN(login_date) from logins where user_id IN 
(SELECT l1.user_id as user_id from logins l1 JOIN logins l2 ON l1.user_id=l2.user_id AND l2.login_date=(l1.login_date-INTERVAL 1 DAY)) GROUP BY user_id;