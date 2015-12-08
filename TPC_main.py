#Main code: December 2015

#Important Notes :
#1) concentration sequence should alwasy be : pmpi, pi4p, pip2, dag, pmpa, erpa, cdpdag, erpi
#2) parameter sequence shuld always be: plc, A, B, C, D, E, alpha, beta, gamma, delta, epsilon

#Initial Imports
import TPC_functions
import TPC_settings as tset
import math, datetime, itertools
import numpy as np
from scipy.integrate import odeint
import matplotlib
matplotlib.use('TkAgg') #For interactive plots
import matplotlib.pyplot as plt


filename = "%s_Time_Para.txt"%(datetime.datetime.now().strftime("%y%m%d%I%M%S"))

pmpi = 21.49
pi4p = 17.00
pip2 = 16.75
dag = 2.72
pmpa = 35.59
erpa = 21.17
cdpdag = 1.11
erpi = 318.63

initial_conditions = [pmpi, pi4p, pip2, dag, pmpa, erpa, cdpdag, erpi] #Concentration vector

for i in itertools.product(tset.A_range, tset.B_range, tset.C_range, tset.D_range, tset.E_range):

    A, B, C, D, E = i
    alpha, beta, gamma, delta, epsilon = 0.05, 0.05, 0.008, 0.167, 0.001
    plc = 0.078

    if (alpha < A) and ((alpha/delta) < E):   #It will scan only parameters with positive concentrations

        parameters = [plc, A, B, C, D, E, alpha, beta, gamma, delta, epsilon]  #Parameter vector
        time = np.linspace(0,tset.time_period,tset.time_integration_points)  #Time grid

        steady_state_concentration = odeint( TPC_functions.generalODE , initial_conditions, time , args=(parameters,))

        pre_analysis_concentrations = steady_state_concentration[-1] #Recoreded steady states
        #PIP2 depletion during light stimulation
        ss_pip2 = pre_analysis_concentrations[2]
        depleted_pip2 = (ss_pip2*tset.percentage_depletion)/100.0
        new_dag = pre_analysis_concentrations[3] + ss_pip2 - depleted_pip2
        #Updating PIP2 and DAG values
        pre_analysis_concentrations[2] = depleted_pip2
        pre_analysis_concentrations[3] = new_dag

        recovery_profile = odeint( TPC_functions.generalODE , pre_analysis_concentrations, time , args=(parameters,))

        desired_pip2_concentration_index =  np.argmax(recovery_profile[:,2]> ((tset.recovery_time_to_monitor*ss_pip2)/100.0))
        percentage_recovery_time = time[desired_pip2_concentration_index]

        time_stamp = datetime.datetime.now().strftime("%y%m%d%I%M%S") #Year,Month,Date,Hour,Minute,Seconds

        final_list = [ss_pip2]+[tset.percentage_depletion]+[percentage_recovery_time] + parameters
        str_conversion = [ float(round(elem,3)) for elem in final_list ]
        str_para = '\t'.join(str(k1) for k1 in str_conversion)


        fh2 = open(filename,'a')
        fh2.write("%s\t%s"%(time_stamp,str_para))
        fh2.write('\n')
        fh2.close()
