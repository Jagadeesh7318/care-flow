import pandas as pd
from google.cloud import bigquery

client = bigquery.client(project="careflow-511810")
df=client.query(
    "select * from `careflow-511810.careflow.event_log`"
).to_dataframe()