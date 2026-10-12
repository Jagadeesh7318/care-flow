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