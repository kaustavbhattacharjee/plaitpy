import plaitpy
import pandas as pd

# Mobile Clinic records
t1 = plaitpy.Template("templates/kb/mobile_clinic.yml")
t1_output = t1.gen_records(100)
mobile_clinic_records = pd.concat([pd.DataFrame(d, index=[1]) for d in t1_output]).reset_index(drop=True)
mobile_clinic_records.to_csv("datasets/mobile_clinic_records.csv",index=False)
#print(mobile_clinic_records)

# County records
t2 = plaitpy.Template("templates/kb/county_records.yml")
t2_output = t2.gen_records(100)
county_records = pd.concat([pd.DataFrame(d, index=[1]) for d in t2_output]).reset_index(drop=True)
county_records.to_csv("datasets/county_records.csv",index=False)
#print(county_records)

# Census records
t3 = plaitpy.Template("templates/kb/census_records.yml")
t3_output = t3.gen_records(100)
census_records = pd.concat([pd.DataFrame(d, index=[1]) for d in t3_output]).reset_index(drop=True)
census_records.to_csv("datasets/census_records.csv",index=False)
print(census_records)