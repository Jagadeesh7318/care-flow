import pandas as pd
from google.cloud import bigquery
client = bigquery.Client(project="careflow-511810")
df=client.query("select * from `careflow-511810.careflow.event_log`").to_dataframe()
df = df.sort_values(["case_id","event_timestamp"])
paths = df.groupby("case_id")["activity_name"].apply(tuple)
ideal=("Registration","Triage","X-Ray","Doctor Consultation","Discharge")
result=pd.DataFrame({"case_id":paths.index,"path":[">".join(p) for p in paths],"compliant":[p==ideal for p in paths],})