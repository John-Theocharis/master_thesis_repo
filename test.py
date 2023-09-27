import pandas as pd

file_path = 'MyData.xlsx'
df = pd.read_excel(file_path)

print(df.head())