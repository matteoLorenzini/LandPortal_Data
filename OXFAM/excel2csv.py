import pandas as pd



xls =  pd.ExcelFile('oxfam.xlsx')

df1 = pd.read_excel(xls, '.csv')


csv = df1[['Indicator ID', 'Indicator name','Company','Country ISO','Country name','Time','Value','Note']]

print(csv)

mapping = csv.rename(columns={	'Indicator ID': 'Col_1','Indicator name': 'Col_1',
								'Company': 'Col_1','Country ISO': 'Col_1','Country name': 'Col_1',
								'Time': 'Col_1','Value': 'Col_1','Note': 'Col_1'}, index={'Indicator ID': 'Col_1'})

print(mapping)



csv.to_csv('oxfam.csv',sep = ';',  index=False, header=True, encoding="utf-8")

