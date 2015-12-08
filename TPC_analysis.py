#Analysis after results from main code
import pandas as pd
import matplotlib, sys, datetime
matplotlib.use('TkAgg') #For interactive plots
import matplotlib.pyplot as plt

current_script_name = sys.argv[0]
time_stamp = datetime.datetime.now().strftime("%d %B %Y")

filename = 'PLC_0_0078_Time_Para.txt'
column_labels = ['timestamp','sspip2','percentdepletion','recoverytime','plc', 'A', 'B', 'C', 'D', 'E', 'alpha', 'beta', 'gamma', 'delta', 'epsilon']
matrix = pd.read_csv(filename,header=None, sep="\t")
matrix.columns=column_labels
#Filter Conditions
parameter_thr = 1
plotarray = matrix
#plotarray= plotarray[plotarray.recoverytime <10]
#plotarray= plotarray[plotarray.A < parameter_thr]
#Plotting
#plt.hist(plotarray.A.values,alpha = 0.5, label = 'A')

matrix2 = pd.read_csv('PLC_0_078_Time_Para.txt',header=None, sep="\t")
matrix2.columns=column_labels
matrix3 = pd.read_csv('PLC_0_78_Time_Para.txt',header=None, sep="\t")
matrix3.columns=column_labels
matrix4 = pd.read_csv('PLC_7_8_Time_Para.txt',header=None, sep="\t")
matrix4.columns=column_labels


plt.hist(plotarray.recoverytime.values,alpha = 0.5,label=r'$\nu = 0.0078$')
plt.hist(matrix2.recoverytime.values,alpha = 0.5,label=r'$\nu = 0.078$')
plt.hist(matrix3.recoverytime.values,alpha = 0.5,label=r'$\nu = 0.78$')
plt.hist(matrix4.recoverytime.values,alpha = 0.5,label=r'$\nu = 7.8$')

plt.legend(loc='best')
plt.xlabel('Recovery Time (min)')
plt.ylabel('Frequency')
plt.title(r'Recovery time at different $\nu_{plc}$ values')
plt.annotate("[ Plotted on %s with \" %s \"] "%(time_stamp,current_script_name), (0.5,0), (0, -50), xycoords='axes fraction', textcoords='offset points',ha="center", va="center",size=9)
plt.savefig('plot_image.png', dpi=300, format='png', bbox_inches='tight')
plt.show()
