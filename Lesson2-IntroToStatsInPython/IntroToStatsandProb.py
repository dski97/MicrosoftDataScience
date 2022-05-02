#import libraries
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

#import data
df = pd.read_csv(r"C:\Users\cwalinskid\Desktop\MicrosoftDataScience\Lesson2-IntroToStatsInPython\SOCR_MLB.tsv", sep='\t', header=None, names=['Name', 'Team', 'Role', 'Height', 'Weight', 'Age'])

#compute the average values for age,height,weight
print(f"Average Age: {df['Age'].mean()}")
print(f"Average Height: {df['Height'].mean()}")
print(f"Average Weight: {df['Weight'].mean()}")

#compute the standard deviation and variance for height
print(f"Standard Deviation: {df['Height'].std()}")
print(f"Variance: {df['Height'].var()}")

import scipy.stats

def mean_confidence_interval(data, confidence = 0.95):
    a = 1.0*np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1+confidence)/2., n-1)
    return m, h

for p in [0.85, 0.90, 0.95]:
    m,h = mean_confidence_interval(df['Weight'].fillna(method='pad'),p)
    print(f"p={p:.2f}, mean={m:.2f}+/-{h:.2f}")

df.groupby('Role').agg({'Height':'mean', 'Weight':'mean', 'Age':'count'}).rename(columns={'Age':'Count'})
print(df.groupby('Role').agg({'Height':'mean', 'Weight':'mean', 'Age':'count'}))

from scipy.stats import ttest_ind

#plot the correlation between height and weight
plt.scatter(df['Height'], df['Weight'])
plt.xlabel('Height')
plt.ylabel('Weight')
plt.show()
