import plaitpy
import pandas as pd
t = plaitpy.Template("templates/timestamp/uniform1.yml")
print(t.gen_record(2))
my_pd = pd.DataFrame(t.gen_record(2))
print(pd)
#print(t.gen_records(10))