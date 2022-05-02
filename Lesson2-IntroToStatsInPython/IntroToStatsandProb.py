#import libraries
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

#create a list of random numbers
sample = [ random.randint(0,10)for _ in range(30)]
print(f"Sample: {sample}")
print(f"Mean: {np.mean(sample)}")
print(f"Variance: {np.var(sample)}")
#plot a histogram of the sample
plt.hist(sample)
plt.show()

#import data