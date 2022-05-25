import plaitpy
import pandas as pd
t = plaitpy.Template("templates/timestamp/uniform1.yml")
#print(t.gen_record(2))
''' my_pd = pd.DataFrame(t.gen_records(2))
print(my_pd) '''
my_pd = t.gen_records(100)
print(my_pd)
#out = pd.DataFrame.from_dict(my_pd, orient='columns')
timeseries_df = pd.concat([pd.DataFrame(d, index=[1]) for d in my_pd]).reset_index(drop=True)
print(timeseries_df)
print()
