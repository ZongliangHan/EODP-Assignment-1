# COMP20008 2021 Semester 1 Assignment 1
Name: Zongliang Han
StudentID: 1166050

this project is the solution for assignment 1.

In part a, a csv file of owid-covid-data-monthly was generated based on the data from https://covid.ourworldindata.org/data/owid-covid-data.csv.
In owid-covid-data-monthly, it collected number of total caeses, new cases, total death, new death and fatality in different countries in every month in 2020.
two scatter plots was genereted based on this csv file. In scatter-a, each dot represent a different locations with number of total cases in 2020 as x axis and case fatality rate as y axis. In scatter-b, it just like scatter-a but with log value of total cases in 2020 as x axis in order to have a better visualisation.

In part b, a csv file of partb1.csv was generated, which collects the information of filename flowwed by its documentID based on the article in folder of cricket. 
then a simpel search programm was write to find the articles based on the key words. and finally similarity score was calculate based the key words and articles. 

list of dependencies
libraries: pands, argparse, re, os, sys, matplotlib.pyplot, numpy, nltk, numpy.lianlg, math, sklearn.feature_extraction.text 
csv files: https://covid.ourworldindata.org/data/owid-covid-data.csv.
text: articles in cricket folder
