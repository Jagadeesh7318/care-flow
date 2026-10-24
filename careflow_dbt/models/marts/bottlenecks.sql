select
    activity_name as from_activity,
    next_activity as to_activity,
    count(*) as patients,
    round(avg(timestamp_diff(next_ts,event_timestamp,minute)),1) as avg_minutes
from (
    select
        activity_name,
        event_timestamp,
        lead(activity_name) over (partition by case_id order by event_timestamp) as next_activity,
        lead(event_timestamp) over (partition by case_id order by event_timestamp) as next_ts
    from {{ ref('stg_events') }}
)
where next_activity is not null
group by 1, 2
order by avg_minutes desc