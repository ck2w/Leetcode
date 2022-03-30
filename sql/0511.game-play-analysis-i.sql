# Write an SQL query to report the first login date for each player.

select player_id, min(event_date) as first_login 
from activity
group by player_id