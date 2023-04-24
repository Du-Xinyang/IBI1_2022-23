import os
from pydoc import describe

import matplotlib
import mpl_toolkits
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# The code for importing the .csv file works
os.chdir("D:/python-learn/02_python入门语法/IBI1")
covid_data = pd.read_csv("full_data.csv")
print(covid_data.head(7))
covid_data.info()
print(covid_data.describe())
print(covid_data.iloc[2,0:5])
print(covid_data.iloc[0:2,:])
print(covid_data.iloc[0:10:2,0:5])
# There is correct code for showing the second column from every 100th row from the first 1000 rows (inclusive)
print(covid_data.iloc[0:1001:100,1])
print(covid_data.iloc[0:3,[0,1,3]])
my_columns = [True, True, False, True, False, False]
print(covid_data.iloc[0:3,my_columns])
print(covid_data.loc[2:4,"date"])
"""
for location in covid_data:
    if "location" == "Afghanistan":
       print(covid_data.iloc[0:,"total_cases"])
       else:
       row = False
    my_lists = [False, row, False, False, False, False]
"""
# You have successfully used a Boolean to show “total cases” for all rows corresponding to Afghanistan.
print(covid_data.loc[covid_data["location"]=="Afghanistan","total_cases"])
# You have correctly computed the mean number of new cases and new deaths on 31 March 2020
my_columns2 = [False, False, True, True, False, False]
print(covid_data.loc[covid_data["date"]=="2020/3/31",my_columns2])
new_data = np.array(covid_data.loc[covid_data["date"]=="2020/3/31",my_columns2],dtype = None, copy = True, order = None, subok = False, ndmin = 0)
print(np.average(new_data,axis=0))
# The mean new cases and new deaths on this date are different, new cases:640.46153846, new deaths: 37.92820513,the proportion of  new deaths as a proportion of the new cases on 31 March is 0.052922
# You have successfully created boxplot of new cases and new deaths on 31 March 2020
# caculate the standard deviation of new_data cases and deaths and print
std=np.std(new_data,axis=0, ddof=1)
print(std)
# boxplot1,scale:标准差，size:样本数
num= np.random.normal(loc=640.46153846,scale=4769.46840846,size=195)
plt.title('new_cases on 31March 2020')
plt.boxplot(num,
            vert=True,
            whis=1.5,
            patch_artist=True,
            showmeans=True,
            meanline=True,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False,
            )
plt.show()
# boxplot2
num= np.random.normal(loc=37.92820513,scale=281.81176538,size=195)
plt.title('new_deaths on 31 March')
plt.boxplot(num,
            vert=True,
            whis=1.5,
            patch_artist=True,
            showmeans=True,
            meanline=True,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False,
            )
plt.show()
# You have successfully plotted both new cases and new deaths worldwide over time
# create new variables
new_cases=new_data[:,0]
new_deaths=new_data[:,1]
plt.xlabel('new_cases')
plt.ylabel('new_deaths')
plt.title('comparing')
plt.plot(new_cases,'p',color='g')
plt.plot(new_deaths,'p',color='blue')# b+:the way to present plots is blue +;r+:red +;bo:blue  dot;p:pentagen  the command is about how the data are presented.
plt.show()
# The code to answer the question runs without errors
# The code to answer the question does what it is meant to do
# Question:Are there places in the World where there have been more than 10,000 total infections(as of 31 March)? If so, where are they?
my_columns3=[False, True, False, False, True, False]
new_data2= np.array(covid_data.loc[covid_data["date"]=="2020/3/31",my_columns3],dtype = None, copy = True, order = None, subok = False, ndmin = 0)
print(new_data2)
total_cases=new_data2[:,1]
countries=new_data2[:,0]
plt.ylabel('countries',fontsize=10)
plt.xlabel('total_cases')
plt.title('total_cases in different countries on31 March')
plt.plot(total_cases,countries,'b+',color='g')
plt.show()
