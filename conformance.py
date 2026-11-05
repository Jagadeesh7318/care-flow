import pandas as pd
from google.cloud import bigquery
#1.Read the event log from BigQuery 
client = bigquery.Client(project="careflow-511810")
df=client.query("select * from `careflow-511810.careflow.event_log`").to_dataframe()
#Build each patient's path in time order
df = df.sort_values(["case_id","event_timestamp"])
paths = df.groupby("case_id")["activity_name"].apply(tuple)
#Compare with the ideal path
ideal=("Registration","Triage","X-Ray","Doctor Consultation","Discharge")
result=pd.DataFrame({"case_id":paths.index,"path":[">".join(p) for p in paths],"compliant":[p==ideal for p in paths],})
#Summary
print(f"Compliant:{result.compliant.mean():.1%}")
print(f"Non-compliant:{(~result.compliant).mean():.1%}")
print(result.path.value_counts())
result.to_csv("conformance_results.csv",index=False)
print("Saved conformance_results.csv")