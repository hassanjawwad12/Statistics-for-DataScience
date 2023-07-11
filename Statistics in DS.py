# -*- coding: utf-8 -*-
"""Muhammad Hassan Jawwad Week2-Day1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13BiI_O6j23RD9BP1OTiYsu18Rf57tZEs
"""

import numpy as np
import statistics

import pandas as pd
df = pd.read_csv('weight-height.csv')
df.head()

df.describe()

df.info()

height = np.array(df['Height'])
print("MEAN HEIGHT : ")
np.mean(height)

weight = np.array(df['Weight'])
print("MEAN WEIGHT : ")
np.mean(weight)

print("Median Height : ")
np.median(height)

print("weight height: ")
np.median(weight)

print("Standard deviation height : ")
np.std(height)

print("Standard deviation weight : ")
np.std(weight)

from scipy.stats import skew
from scipy.stats import kurtosis

skew(height, axis=0, bias=True)

skew(weight, axis=0, bias=True)

kurtosis(height, axis=0, bias=True)

kurtosis(weight, axis=0, bias=True)

