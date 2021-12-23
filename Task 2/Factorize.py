# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Wuzzuf_Jobs.csv')

# X = dataset.iloc[:100, :].values

dataset['NEW'] = pd.factorize(dataset['YearsExp'])[0]
x = dataset.iloc[:,[5,-1]]
print(x)
