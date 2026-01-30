
#program to determine whether person survives on the titanic or not

#Imports

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# Datasets
titanic = pd.read_csv('/Users/shivamshsthavara/Documents/projects/titanic project/train.csv')
test = pd.read_csv('/Users/shivamshsthavara/Documents/projects/titanic project/test.csv')

# exploring the data
print(titanic.head())
print(titanic.isnull().sum())
print(titanic.info())

#found cabin and age to be high in missing values with embarked only having 2 missing values

