#Code functions


#ODE function

def generalODE(con, time, parameters):
    plc, A, B, C, D, E, alpha, beta, gamma, delta, epsilon = parameters #Set up Parameters
    pmpi, pi4p, pip2, dag, pmpa, erpa, cdpdag, erpi = con #set up concentrations

    vpitp = A*plc
    v4tase = B*plc
    v5tase = C*plc
    vpap = D*plc
    vpatp = E*plc
    vpi4k = ((A*(alpha + (beta*B)))/(A-alpha))*plc
    vpip5k = ((alpha*(C + 1.0))/(beta))*plc
    vdagk = ((alpha*(E+D))/(gamma*E))*plc
    vcds = ((alpha*E)/((delta*E)-alpha))*plc
    vpis = (alpha/epsilon)*plc
    vplc = plc

    f_pmpi = (vpitp*erpi) + (v4tase*pi4p) - (vpi4k*pmpi)
    f_pi4p = (vpi4k*pmpi) + (v5tase*pip2) - ((vpip5k + v4tase)*pi4p)
    f_pip2 = (vpip5k*pi4p) - ((v5tase + vplc)*pip2)
    f_dag = (vplc*pip2) + (vpap*pmpa) - (vdagk*dag)
    f_pmpa = (vdagk*dag) - ((vpatp + vpap)*pmpa)
    f_erpa = (vpatp*pmpa) - (vcds*erpa)
    f_cdpdag = (vcds*erpa) - (vpis*cdpdag)
    f_erpi = (vpis*cdpdag) - (vpitp*erpi)

    return [f_pmpi, f_pi4p, f_pip2, f_dag, f_pmpa, f_erpa, f_cdpdag, f_erpi]
