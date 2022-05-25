import plaitpy
t = plaitpy.Template("templates/timestamp/uniform1.yml")
print(t.gen_record())
print(t.gen_records(10))