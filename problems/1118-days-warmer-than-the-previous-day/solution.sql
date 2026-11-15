-- your query
SELECT w1.recorded_on FROM weather w1 JOIN weather w2 ON w2.recorded_on = (w1.recorded_on-INTERVAL 1 DAY) where w1.temperature>w2.temperature ORDER by recorded_on;

