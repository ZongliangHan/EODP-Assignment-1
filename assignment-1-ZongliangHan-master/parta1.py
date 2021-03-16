import pandas as pd
import argparse
#read csc file and extract dataframe
covid_data = pd.read_csv('assignment-1-ZongliangHan-master/owid-covid-data.csv', encoding = 'ISO-8859-1')
countries = covid_data.iloc[:,2]
data_body = covid_data.iloc[:,[2, 3, 4, 5, 7, 8]]

#extract date text and store it as month and year
date = covid_data['date']
month = []
year = []
for i in date:
    i = i[0:7]
    j = i[0:4]
    month.append(i)
    year.append(j)
month = pd.Series(month)
year = pd.Series(year)
month.index
year.index
data_body['month']=month

#delete the data of year 2021 and reorganise dataframe
data_body.index = year
data_body = data_body.loc[['2020'],['location', 'month', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths']]

#calculating the data based on location and month
organised_data = data_body.groupby(['location', 'month']).sum()
print (organised_data)
