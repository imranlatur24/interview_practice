import pandas as pd
# Creating a DataFrame with different data types from a list of lists
data = [['Geek1', 28, 'Engineer'],
		['Geek2', 25, 'Data Scientist'],
		['Geek3', '32', 'Manager']] # Age represented as a string
columns = ['Name', 'Age', 'Occupation']
df = pd.DataFrame(data, columns=columns)
df['Age'] = pd.to_numeric(df['Age'], errors='coerce') # Convert 'Age' column to numeric, handling errors
print(df)
