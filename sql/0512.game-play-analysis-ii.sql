# Write an SQL query to report the device that is first logged in for each player.

select player_id, device_id 
from activity
where (player_id, event_date) in (
    select player_id, min(event_date)
    from activity
    group by player_id
)