from __future__ import print_function
from ortools.linear_solver import pywraplp
import time

def model(packages,cargo):
    solver = pywraplp.Solver('Model2D', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    # importo dimensioni dei pacchi e del camion

    n=len(packages)

    w =[packages[i].getW() for i in range(n)]
    d =[packages[i].getD() for i in range(n)]

    W =cargo.getW()
    D =solver.IntVar(0,solver.infinity(),"D")

    Md=sum(d)
    Mw=W+min(w)

    # definisco le variabili
    s1 =[[solver.IntVar(0,1,"s1%d%d" % (i,j)) for i in range(n)] for j in range(n)]
    s2 =[[solver.IntVar(0,1,"s2%d%d" % (i,j)) for i in range(n)] for j in range(n)]
    s3 =[[solver.IntVar(0,1,"s3%d%d" % (i,j)) for i in range(n)] for j in range(n)]
    s4 =[[solver.IntVar(0,1,"s4%d%d" % (i,j)) for i in range(n)] for j in range(n)]

    x =[solver.IntVar(0,solver.infinity(),"x%d" % i) for i in range(n)]
    y =[solver.IntVar(0,solver.infinity(),"y%d" % i) for i in range(n)]

    # definisco i constraints
    for i in range(n):
        for j in range(n):
            if(i < j):
                solver.Add(x[i] + w[i] <= x[j] + Mw*(1-s1[i][j]))           #(1)
                solver.Add(y[i] + d[i] <= y[j] + Md*(1-s2[i][j]))           #(2)
                solver.Add(x[j] + w[j] <= x[i] + Mw*(1-s3[i][j]))           #(3)
                solver.Add(y[j] + d[j] <= y[i] + Md*(1-s4[i][j]))           #(4)
                solver.Add(s1[i][j]+s2[i][j]+s3[i][j]+s4[i][j]>=1)          #(5)
        solver.Add(x[i] + w[i] <= W)                                        #(6)
        solver.Add(y[i] + d[i] <= D)                                        #(6)

    #funzione obiettivo
    objective = solver.Objective()
    objective.SetCoefficient(D,1)
    objective.SetMinimization()

    #soluzione
    print(solver.Solve())

    print("larghezza camion: ",W)
    print("lunghezza migliore: ",D.solution_value())
    print ("larghezze: ",w)
    print ("lungo:     ",d)
    for i in range(n):
        print("oggetto n: ",i," coordinate:",x[i].solution_value()," ",y[i].solution_value())
