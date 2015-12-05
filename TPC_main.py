#Main code: December 2015
#General use code
#main code file
#Initial Imports
import TPC_functions
import TPC_settings as tset
import math
import numpy as np
from scipy.integrate import odeint
import matplotlib
matplotlib.use('TkAgg') #For interactive plots
import matplotlib.pyplot as plt

pmpi = 21.49
pi4p = 17.00
pip2 = 16.75
dag = 2.72
pmpa = 35.59
erpa = 21.17
cdpdag = 1.11
erpi = 318.63

initial_conditions = [pmpi, pi4p, pip2, dag, pmpa, erpa, cdpdag, erpi]
A, B, C, D, E = 0.5, 0.1, 0.1, 0.1, 0.3
alpha, beta, gamma, delta, epsilon = 0.05, 0.05, 0.008, 0.167, 0.001
plc = 1.0

parameters = [plc, A, B, C, D, E, alpha, beta, gamma, delta, epsilon]

time = np.linspace(0,tset.time_period,tset.time_integration_points)
concentration_profile = odeint( TPC_functions.generalODE , initial_conditions, time , args=(parameters,))

final_concentrations = concentration_profile
final_time = time

pPMPI = final_concentrations[:, 0]
pPI4P = final_concentrations[:, 1]
pPIP2 = final_concentrations[:, 2]
pDAG= final_concentrations[:, 3]
pPMPA= final_concentrations[:, 4]
pERPA= final_concentrations[:, 5]
pCDPDAG= final_concentrations[:, 6]
pERPI= final_concentrations[:, 7]
plt.plot(final_time, pPMPI, label='PMPI',linewidth=2.0)
plt.plot(final_time, pPI4P, label='PI4P',linewidth=2.0)
plt.plot(final_time, pPIP2, label='PIP2',linewidth=2.0)
plt.plot(final_time, pERPI, label='ERPI',linewidth=2.0)
plt.plot(final_time, pDAG, label='DAG',linewidth=2.0)
plt.plot(final_time, pPMPA, label='PMPA',linewidth=2.0)
plt.plot(final_time, pERPA, label='ERPA',linewidth=2.0)
plt.plot(final_time, pCDPDAG, label='CDPDAG',linewidth=2.0)

plt.legend(loc=0)
plt.show()
