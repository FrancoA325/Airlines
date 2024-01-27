import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

crashIn = pd.read_csv('/Users/fantunez/Documents/dataMining/data/Airplane_Crashes_and_Fatalities_Since_1908_20190820105639.csv')
print(crashIn.describe())