import pandas as pd
import argparse
import matplotlib.pyplot as plt
import numpy as np

#extract useful data
covid_data = pd.read_csv('owid-covid-data-2020-monthly.csv')
total_cases_month = covid_data.iloc[:,[0,3]]
total_cases_year = total_cases_month.groupby('location').last()
total_deaths_month = covid_data.iloc[:,[0,5]]
total_deaths_year = total_deaths_month.groupby('location').last()
case_fatality_rate = total_deaths_year.iloc[:,0]/total_cases_year.iloc[:,0]

#plot scatter with case fatality rate as y value and new cases in 2020 as x value
plt.scatter(total_cases_year, case_fatality_rate, s=20, color = 'blue')
plt.ylabel('case_fatality_rate')
plt.xlabel('new_cases_in_2020')
plt.grid(True)
plt.savefig('scatter-a.png')
plt.show()


#change the x value to log value
new_x = np.log(total_cases_year)
plt.scatter(new_x, case_fatality_rate, s=20, color = 'blue')
plt.ylabel('case_fatality_rate')
plt.xlabel('log_new_cases_in_2020')
plt.grid(True)
plt.savefig('scatter-b.png')
plt.show()
