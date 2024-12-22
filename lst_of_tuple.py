import pandas as pd

lst=[('imran',31),
    ('irfan',27),
    ('afreen',28)
     ]
df=pd.DataFrame(lst)
df2=pd.DataFrame.from_records(lst)
print(df)
print()
print(df2)
df.columns = ['Names','Age']
print(df.transpose())