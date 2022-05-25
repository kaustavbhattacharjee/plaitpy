import plaitpy
t = plaitpy.Template("uniform1.yml")
print(t.gen_record())
print(t.gen_records(10))