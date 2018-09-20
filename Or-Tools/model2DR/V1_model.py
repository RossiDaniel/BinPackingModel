from __future__ import print_function
from ortools.linear_solver import pywraplp
import timeit

def model(packages,cargo):
    solver = pywraplp.Solver('Model2DR', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    # importo dimensioni dei pacchi e del camion
    n=len(packages)

    w =[packages[i].getW() for i in range(n)]
    d =[packages[i].getD() for i in range(n)]

    print(w)
    print(d)

    W =cargo.getW()
    D =solver.IntVar(0,solver.infinity(),"D")

    Md=sum(d)
    Mw=W+min(w)

    # definisco le variabili
    l =[[solver.BoolVar("l%d%d" % (i,j)) for i in range(n)] for j in range(n)]
    b =[[solver.BoolVar("b%d%d" % (i,j)) for i in range(n)] for j in range(n)]
    r =[solver.BoolVar("r%d" % (i)) for i in range(n)]

    x =[solver.IntVar(0,solver.infinity(),"x%d" % i) for i in range(n)]
    y =[solver.IntVar(0,solver.infinity(),"y%d" % i) for i in range(n)]



    # definisco i constraints
    for i in range(n):
        for j in range(n):
            if(i < j):
                solver.Add(l[i][j] + l[j][i] + b[i][j] + b[j][i] >= 1)                           #(1)
            if(i != j):
                solver.Add(x[i] - x[j] + Mw * l[i][j] <= Mw - w[i]*r[i] - d[i]*(1-r[i]))         #(2)
                solver.Add(y[i] - y[j] + Md * b[i][j] <= Md - d[i]*r[i] - w[i]*(1-r[i]))         #(3)
        solver.Add(x[i] + w[i]*r[i] + d[i]*(1-r[i]) <= W)                                        #(4)
        solver.Add(y[i] + d[i]*r[i] + w[i]*(1-r[i]) <= D)                                        #(5)

    #funzione obiettivo
    objective = solver.Objective()
    objective.SetCoefficient(D,1)
    objective.SetMinimization()

    #soluzione
    solver.Solve()

    #lista soluzioni
    s = []
    for i in range(n):
        s.append([x[i].solution_value(), y[i].solution_value(), i, r[i].solution_value()])
    return s