import pandas as pd
# Bitte noch folgende Module installieren
# pip install matplotlib
# pip install openpyxl

df = pd.read_csv('data_dup.csv')
print(df)

x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True)

print(df.to_string())

