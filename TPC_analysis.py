#Analysis after results from main code
import pandas as pd
import matplotlib
matplotlib.use('TkAgg') #For interactive plots
import matplotlib.pyplot as plt

filename = '151207110209_Time_Para.txt'
column_labels = ['timestamp','sspip2','percentdepletion','recoverytime','plc', 'A', 'B', 'C', 'D', 'E', 'alpha', 'beta', 'gamma', 'delta', 'epsilon']
matrix = pd.read_csv(filename,header=None, sep="\t")
matrix.columns=column_labels
plotarray= matrix[matrix.recoverytime < 10]
plt.hist(plotarray.recoverytime.values,100)
plt.show()
