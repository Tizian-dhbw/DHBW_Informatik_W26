import pandas as pd

# Bitte noch folgende Module installieren
# pip install matplotlib
# pip install openpyxl

df = pd.read_csv('Data_dup.csv')
print(df)
df_dupResul=df.duplicated()
i=0
print(df_dupResul)


for Ergebnis in df_dupResul:
    print(Ergebnis)
    # zählen sie alle dupilicates


print(i)



# löschen sie die duplicates und behalten sie den ersten Eintrag



df_dupResul=df.duplicated()
print(df_dupResul)
df.to_excel("Data_dup2.xlsx")


