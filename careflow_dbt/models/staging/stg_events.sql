select
   upper(trim(patient_id)) as case_id,
   initcap(trim(activity)) as activity_name,
   safe_cast(event_time as timestamp) as event_timestamp,
   doctor,
   age  as age_group
from {{ source('careflow','raw_events') }}
where patient_id is not null
 and safe_cast(event_time as timestamp) is not null
 qualify row_number() over (
    partition by upper(trim(patient_id)), initcap(trim(activity)),event_time
    order by event_time)=1
 