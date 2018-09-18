from __future__ import print_function
from ortools.linear_solver import pywraplp

def model2D(packages,cargo):
    solver = pywraplp.Solver('Model2D', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
    # importo dimensioni dei pacchi e del camion
    n=len(packages)

    w =[packages[i].getW() for i in range(n)]
    d =[packages[i].getD() for i in range(n)]

    W =cargo.getW()
    D =cargo.getD()

    # definisco le variabili
    l =[[solver.BoolVar("l%d%d" % (i,j)) for i in range(n)] for j in range(n)]
    b =[[solver.BoolVar("l%d%d" % (i,j)) for i in range(n)] for j in range(n)]

    x =[solver.NumVar(0,solver.infinity(),"x%d" % i) for i in range(n)]
    y =[solver.NumVar(0,solver.infinity(),"y%d" % i) for i in range(n)]

    s=solver.NumVar(0,solver.infinity(),"s")

    # definisco i constraints
    for i in range(n):
        for j in range(n):
            if(i < j):
                solver.Add(l[i][j] + l[j][i] + b[i][j] + b[j][i] >= 1)
            if(i != j):
                solver.Add(x[i] - x[j] + W * l[i][j] <= W - w[i])
                solver.Add(y[i] - y[j] + D*b[i][j] <= D - d[i])

        solver.Add(x[i] <= W - w[i])
        solver.Add(y[i] <= D - d[i])
        solver.Add(s >= y[i] + d[i])

    #funzione obiettivo
    objective = solver.Objective()
    objective.SetCoefficient(s,1)
    objective.SetMinimization()

    #soluzione
    solver.Solve()
    for i in range(n):
        print(x[i].solution_value()," ",y[i].solution_value())
    for i in range(n):
        for j in range(n):
            print(i," ",j," ",b[i][j].solution_value())