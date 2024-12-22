# convert 2d list into column using dataframe
import pandas as pd
lst=[['imran',31],['irfan',21]]
columns=['Name','Age']
df = pd.DataFrame(lst,columns=columns)
print(df)

# convert 2d list into column using dataframe using from_records()
df2 = pd.DataFrame.from_records(lst,columns=columns)
print(df2)

# convert 2d list into column using dataframe using from_dict()
df3=pd.DataFrame.from_dict(dict(zip(columns,zip(*lst))))
print(df3)