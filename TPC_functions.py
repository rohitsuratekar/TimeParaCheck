#Code functions


#ODE function


def generalODE(con, time, parameters):

    A, B, C, D, E, alpha, beta, gamma, delta, epsilon = parameters #Set up Parameters
    pmpi, pi4p, pip2, dag, pmpa, erpa, cdpdag, erpi = con #set up concentrations

    f_pmpi = (A*erpi) + (B*pi4p) - (((A*(alpha + (beta*B)))/(A-alpha))*pmpi)
    f_pi4p = (((A*(alpha + (beta*B)))/(A-alpha))*pmpi) + (C*pip2) - ((( (alpha*(C+1.0))/(beta) ) + B)*pi4p)
    f_pip2 = ((( (alpha*(C+1.0))/(beta) ) + B)*pi4p) - ((C+1.0)*pip2)
    f_dag =  pip2 + (D*pmpa) - (((alpha*(E+D))/(gamma*E))*dag)
    f_pmpa = (((alpha*(E+D))/(gamma*E))*dag) - ((E+D)*pmpa)
    f_erpa = (E*pmpa) - (((alpha*E)/((delta*E)- alpha))*erpa)
    f_cdpdag = (((alpha*E)/((delta*E)- alpha))*erpa) - (((alpha)/(epsilon))*cdpdag)
    f_erpi = (((alpha)/(epsilon))*cdpdag) - (A*erpi)

    return [f_pmpi, f_pi4p, f_pip2, f_dag, f_pmpa, f_erpa, f_cdpdag, f_erpi]
