# Convert a 2D dictionary into a DataFrame and then transpose it
import pandas as pd
mydic = {
    'Names': ['imran', 'irfan', 'afreen'],
    'Age': [31, 27, 26]}
# Create a DataFrame from the dictionary
df = pd.DataFrame(mydic)
# Transpose the DataFrame (rows become columns and columns become rows)
print(df.transpose())
