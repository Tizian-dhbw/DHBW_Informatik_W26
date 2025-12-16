import pandas as pd

df = pd.read_csv('Data_dup.csv')
#df = pd.read_excel('Data_dup3.xlsx')

print(df)
df.dropna(inplace = True)

print(df)


# for index,row in df.iterrows():
#     print(row)
#     print(index,row.Duration, row.Calories)
#     print()
#     if index == 5:
#         df.loc[index, 'Calories'] = 45

# print(df.to_string)
df.to_excel("data1_new.xlsx")


