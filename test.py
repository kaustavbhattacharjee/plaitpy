import plaitpy
import pandas as pd
t = plaitpy.Template("templates/kb/mobile_clinic.yml")
my_pd = t.gen_records(100)
#print(my_pd)
timeseries_df = pd.concat([pd.DataFrame(d, index=[1]) for d in my_pd]).reset_index(drop=True)
print(timeseries_df)

