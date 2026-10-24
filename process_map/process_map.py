import pm4py
from google.cloud import bigquery 

client = bigquery.Client(project="careflow-511810")
df=client.query("select * from `careflow-511810.careflow.event_log`").to_dataframe()
df=pm4py.format_dataframe(
    df,
    case_id="case_id",
    activity_key="activity_name",
    timestamp_key="event_timestamp",
)
dfg,start,end=pm4py.discover_dfg(df)
pm4py.save_vis_dfg(dfg,start,end,"as_is_map.png")
print("Saved as_is_map.png")