import pycountry
import pandas as pd


xls =  pd.ExcelFile('input.xlsx')


df1 = pd.read_excel(xls, 'Data')


df1 = df1.rename(columns={'Country Name': 'CountryName','Country (ISO code)':'CountryISOcode'})


def findCountryAlpha3 (country_name):
    try:
        return pycountry.countries.get(name=country_name).alpha_3
    except:
        return ("not founded!")

df1['country_alpha_3'] = df1.apply(lambda row: findCountryAlpha3(row.CountryName) , axis = 1)


print(df1)

df1.to_excel ('excel_iso.xlsx', index = None, header=True)