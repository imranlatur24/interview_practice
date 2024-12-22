# convert 2d list into column using dataframe
import pandas as pd
mydic={
    'Names':['imran','irfan','afreen'],
    'Age':[31,27,26]
}
columns=['N','A']
df = pd.DataFrame(mydic,index=['Soft Engi','Contractor','Tester'])
# rename the column
#df.columns = ['N', 'A']  # Rename the columns way 1
df.columns=columns # Rename the columns way 1
print(df)
