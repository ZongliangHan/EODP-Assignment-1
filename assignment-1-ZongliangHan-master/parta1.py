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
data_body_new = data_body.loc[['2020'],['location', 'month', 'new_cases', 'new_deaths']]
data_body_total = data_body.loc[['2020'],['location', 'month', 'total_cases', 'total_deaths']]

#integreting the tolal_cases and total deaths based on location and month
data_body_total = data_body_total.groupby(['location','month']).max()

#calculating the new cases and new deaths based on location and month
data_body_new = data_body_new.groupby(['location', 'month']).sum()

#combine two data frame and reorganise it
joined_data_body = pd.concat([data_body_new, data_body_total], axis = 1)
column_names = ['total_cases', 'new_cases', 'total_deaths', 'new_deaths']
organised_data = joined_data_body.reindex(columns = column_names)
print (organised_data)
