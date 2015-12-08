#Analysis after results from main code
import pandas as pd
import matplotlib, sys, datetime
matplotlib.use('TkAgg') #For interactive plots
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

current_script_name = sys.argv[0]
time_stamp = datetime.datetime.now().strftime("%d %B %Y")

column_labels = ['timestamp','sspip2','percentdepletion','recoverytime','plc', 'A', 'B', 'C', 'D', 'E', 'alpha', 'beta', 'gamma', 'delta', 'epsilon']

matrix1 = pd.read_csv('PLC_0_0078_Time_Para.txt',header=None, sep="\t")
matrix1.columns=column_labels
matrix2 = pd.read_csv('PLC_0_078_Time_Para.txt',header=None, sep="\t")
matrix2.columns=column_labels
matrix3 = pd.read_csv('PLC_0_78_Time_Para.txt',header=None, sep="\t")
matrix3.columns=column_labels
matrix4 = pd.read_csv('PLC_7_8_Time_Para.txt',header=None, sep="\t")
matrix4.columns=column_labels

fig, ax = plt.subplots(figsize=[9,7.5])
plt.xlabel('Recovery Time (min)')
plt.ylabel('Frequency')
plt.title(r'Distribution of recovery times at different $\nu_{plc}$ values')
plt.annotate("[ Plotted on %s with \" %s \"] "%(time_stamp,current_script_name), (0.5,0), (0, -50), xycoords='axes fraction', textcoords='offset points',ha="center", va="center",size=9)

ax.hist(matrix1.recoverytime.values,alpha = 0.5,color = 'b',label=r'$\nu = 0.0078$')
ax.hist(matrix2.recoverytime.values,alpha = 0.5,color = 'c',label=r'$\nu = 0.078$')
ax.hist(matrix3.recoverytime.values,alpha = 0.5,color = 'r',label=r'$\nu = 0.78$')
ax.hist(matrix4.recoverytime.values,alpha = 0.5,color = 'g',label=r'$\nu = 7.8$')
plt.legend(loc='upper left', bbox_to_anchor=(1, 0.5))

left, bottom, width, height = [0.5, 0.6, 0.3, 0.2]
ax2 = fig.add_axes([left, bottom, width, height])
ax2.hist(matrix3.recoverytime.values,color = 'r',alpha = 0.5)
ax2.hist(matrix4.recoverytime.values,color = 'g',alpha = 0.5)
plt.yticks(visible=False)

plt.savefig('plot_image.png', dpi=300, format='png', bbox_inches='tight')
plt.show()
