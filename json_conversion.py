import pandas as pd
# Create a list of dictionaries, each representing a record with 'name' and 'age' keys
lstpayload = [
    {'name': 'imran', 'age': 31},
    {'name': 'irfan', 'age': 27},
    {'name': 'sonu', 'age': 22},]
# Print the type of the data structure to confirm it's a list
print(type(lstpayload))
# Normalize the list of dictionaries into a tabular DataFrame format
df = pd.json_normalize(lstpayload)
# Print the resulting DataFrame
print(df)
