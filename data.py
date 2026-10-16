import random
import pandas as pd
from datetime import datetime, timedelta

random.seed(42)

DOCTORS = ["Dr. Smith", "Dr. Johnson", "Dr. Williams", "Dr. Brown"]
AGE_GROUPS = ["0-17","18-40","41-65","65+"]
NUM_PATIENTS=5000
LOOPBACK_RATE=0.40

rows=[]

def log(case_id,activity,time,doctor,age_group):
    rows.append({"patient_id":case_id,
                 "activity":activity,
                 "event_time":time.strftime("%Y-%m-%d %H:%M:%S"),
                 "doctor":doctor,
                 "age":age_group})
for i in range(NUM_PATIENTS):
    case_id = f"case{i:05d}"
    doctor = random.choice(DOCTORS)
    age_group = random.choice(AGE_GROUPS)
    time = datetime(2026,1,1)+timedelta(minutes=random.randint(0,60*24*90))
    log(case_id,"REGISTRATION",time,doctor,age_group)
    time += timedelta(minutes=random.randint(5,20))
    log(case_id,"TRIAGE",time,doctor,age_group)
    time += timedelta(minutes=random.randint(10,30))
    log(case_id,"X-RAY",time,doctor,age_group)
    time += timedelta(minutes=random.randint(15,40))
    if random.random()< LOOPBACK_RATE:
        log(case_id,"TRIAGE",time,doctor,age_group)
        time += timedelta(minutes=random.randint(20,50))
    log(case_id,"Doctor Consultation",time,doctor,age_group)
    time += timedelta(minutes=random.randint(10,30))
    log(case_id,"Discharge",time,doctor,age_group)
df=pd.DataFrame(rows)
df=pd.concat([df,df.sample(50,random_state=1)],ignore_index=True)
df.to_csv("ehr_raw.csv",index=False)
print(f"created ehr_raw.csv with {len(df)} rows")