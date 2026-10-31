import pandas as pd
from google.cloud import bigquery

client = bigquery.client(project="careflow-511810")
df=client.query(
    "select * from `careflow-511810.careflow.event_log`"
).to_dataframe()
df = df.sort_values(["case_id","event_timestamp"])
df["next_activity"]=df.groupby("case_id")["activity_name"].shift(-1)
df["next_time"] = df.groupby("case_id")["event_timestamp"].shift(-1)
df["minutes"]=(df["next_time"]- df["event_timestamp"]).dt.total_Seconds()60