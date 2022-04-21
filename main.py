import pandas as pd

df = pd.read_csv('szeptember.csv', encoding=("latin2"), sep=';')
#column_list = list(df)

#2 mulasztott orak
osszes_mul = df['Mulasztott órák'].sum()

print(f'2.feladat \n\t Összes mulasztott órák száma: {osszes_mul}')

#3 bekeres
nap = int(input('kérem adjon meg egy napot (1-30): ')) 
nev = input('diak neve (pontosan ékezetekkel): ')

#4hianyzott-e
hianyzott = False
for index in df.index:
    if df['Név'][index] == nev:
        print(f'4.feladat \n\t A tanuló hiányzott szeptemberben')
        hianyzott = True
if hianyzott == False:
    print(f'4.feladat \n\t A tanuló nem hiányzott szeptemberben')

#5 bekert napon hianyoztak
print(f"5.feladat: hiányzások 2017.09.{nap}.-én:")
for index in df.index:
    if df['Első nap'][index] == nap or df['Utolsó nap'][index] == nap:
        print(f'\t { df["Név"][index]} ({df["Osztály"][index]})')

#6 hianyzasok száma osztalyonkent (csak pandas segitseggel):::::::::::::.......
'''nem jottem ra még'''
