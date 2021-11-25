import pandas as pd



xls =  pd.ExcelFile('oxfam.xlsx')

df1 = pd.read_excel(xls, '.csv')


csv = df1[['Indicator ID', 'Indicator name','Company','Country ISO','Country name','Time','Value','Note']]

print(csv)

mapping = csv.rename(columns={	'Indicator ID': 'ID','Indicator name': 'Title',
								'Company': 'Company','Country ISO': 'Country/ISO','Country name': 'Country/Name',
								'Time': 'Time','Value': 'Value','Note': 'Note'}, index={'Indicator ID': 'ID'})

print(mapping)



mapping.to_csv('oxfam.csv',sep = ';',  index=False, header=True, encoding="utf-8")

