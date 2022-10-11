# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 14:11:36 2022

@author: Sam clastine Jesumuthu
"""

# Exercises Part-1

# 1. Count the number of rows in the csv file you've chosen.
import csv     # imports the csv module
import sys      # imports the sys module
import pandas as pd

data01=open('TB_burden_countries_2022-10-11.csv')
data02=open('TB_data_dictionary_2022-10-11.csv')

count=0

for row in csv.reader(data01):
    count+=1
    
print("Total number of rows : " , count)



# 2. Pick one of the columns with numeric data and calculate the average value using a loop (not a library function such as avg(), we'll come to those soon). One candidate is the column with the name "e_prev_num_lo" which is "Estimated prevalence of TB (all forms), low bound" according to the dictionary here.
data01=open('TB_burden_countries_2022-10-11.csv')

SumOfAllElements=0

for row in csv.reader(data01):    
    try:
        row[16]=float(row[16])
        a=float(row[16])
        SumOfAllElements=a+SumOfAllElements       
        print(SumOfAllElements)    
    except Exception:
        pass
    
lengthOfData=len(row)
print(lengthOfData)
Average=SumOfAllElements/lengthOfData
print("Average: " ,Average)

    # if row[0]=='India' & int(float(row[16]))>15:
    #     print(row)
    
    
    
    
    

#Now, repeat step-2 above but this time find the averages for years 1990 and 2011. Have you observed any difference?


data01=open('TB_burden_countries_2022-10-11.csv')

SumOfAllElements=0

for row in csv.reader(data01):    
    try:
        row[5]=int(row[5])
        if row[5]==2011:
            row[16]=float(row[16])
            a=float(row[16])
            SumOfAllElements=a+SumOfAllElements       
            print(SumOfAllElements)    
    except Exception:
        pass
    
lengthOfData=len(row)
print(SumOfAllElements)
Average=SumOfAllElements/lengthOfData
print("Average: " ,Average)






# df = pd.read_csv('TB_burden_countries_2022-10-11.csv')
# fdata=df.loc[(df.year==2011)]
# SumOfAllElements=0
# lengthOfData=len(fdata)
# print("lengthOfData: ",lengthOfData)
# for val in fdata.e_inc_tbhiv_100k:
#     SumOfAllElements=val+SumOfAllElements
#     print("SumOfAllElements",SumOfAllElements)
# Average=SumOfAllElements/lengthOfData
# print("Average: " ,Average)

#################################EXERCISE-2####################################



import numpy as np
import matplotlib.pyplot as plt


# Create an array of int ranging from 5-15

arr= np.arange(5,15,1)
arr



# Create an array containing 7 evenly spaced numbers between 0 and 23

arr= np.arange(0,23,7)
arr

# Numpy has several routines for generating artificial data following a particular structure. Check this page for different types. And generate an artificial numpy array with values between -1 and 1 that follow a uniform data distribution.

sampleArr = np.random.uniform(-1,1,[15,5])
sampleArr

# Visualise the array in an histogram in matplotlib.

count, bins, ignored = plt.hist(sampleArr, 4, density=True)
plt.plot(bins, np.ones_like(bins), linewidth=3, color='blue')
plt.show()


# Create two random numpy arrays with 10 elements. Find the Euclidean distance between the arrays using arithmetic operators, hint: numpy has a sqrt function

arr1= np.random.randint(25,87, size=10)
arr1
arr2=np.random.randint(17,65, size=10)
arr2
sum=0
for i in range(0,10):
    v=(arr1[i]-arr2[i])**2
    sum=sum+v
    
ed=np.sqrt(sum)
print("Euclidean distance between the arrays :" , ed)