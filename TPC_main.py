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


initial_conditions = [10,10,10,10,10,10,10,10]
A, B, C, D, E = 1, 1, 1, 1, 1
alpha, beta, gamma, delta, epsilon = 0.005, 0.005, 0.0008, 0.167, 0.0001

parameters = [A, B, C, D, E, alpha, beta, gamma, delta, epsilon]

time = np.linspace(0,tset.time_period,tset.time_integration_points)
concentration_profile = odeint( TPC_functions.generalODE , initial_conditions, time , args=(parameters,))
