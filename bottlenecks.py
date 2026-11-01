import pandas as pd
from google.cloud import bigquery

client = bigquery.client(project="careflow-511810")
df=client.query(
    "select * from `careflow-511810.careflow.event_log`"
).to_dataframe()
df = df.sort_values(["case_id","event_timestamp"])
df["next_activity"]=df.groupby("case_id")["activity_name"].shift(-1)
df["next_time"] = df.groupby("case_id")["event_timestamp"].shift(-1)
df["minutes"]=(df["next_time"]- df["event_timestamp"]).dt.total_Seconds()
bottlenecks = (df.dropna(subset=["next_activity"])
               .groupby(["activity_name","next_activity"])["minutes"].agg(patients="count",avg_minutes="mean",max_minutes="max").round(1)
               .reset_index()
               .sort_values("avg_minutes",ascending=False)
)
print(bottlenecks.to_string(index=False))
bottlenecks.to_csv("bottlenecks.csv",index=False)
print("saved bottlenecks.csv")