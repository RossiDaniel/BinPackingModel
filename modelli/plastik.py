from __future__ import print_function
from ortools.linear_solver import pywraplp

"""ESEMPIO TRATTO DA: ESERCIZI RISOLTI DI RICERCA OPERATIVA """
"""ESEMPIO 1.1 PAG 2"""

def algo():
    # Istanzio Glop solver, naming it LinearExample.
    solver = pywraplp.Solver('LinearExample', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    #creo le variabili x1,x2,x3
    x=[]
    for i in range(0,3):
        x.append(solver.NumVar(0,solver.infinity(),'x'))

    #constraint 1: 2x1 + 2x2 + x3 >= 10000
    constraint1 = solver.Constraint(10000,solver.infinity())
    constraint1.SetCoefficient(x[0],2)
    constraint1.SetCoefficient(x[1],2)
    constraint1.SetCoefficient(x[2],1)

    #constraint 2: 2x1 + 3x2 + 2x3 >= 180000
    constraint2 = solver.Constraint(180000,solver.infinity())
    constraint2.SetCoefficient(x[0],2)
    constraint2.SetCoefficient(x[1],3)
    constraint2.SetCoefficient(x[2],2)

    #constraint 3: x1 + x2 + 5x3 >= 20000
    constraint3 = solver.Constraint(20000,solver.infinity())
    constraint3.SetCoefficient(x[0],1)
    constraint3.SetCoefficient(x[1],1)
    constraint3.SetCoefficient(x[2],5)

    # Objective function: .
    objective = solver.Objective()
    objective.SetCoefficient(x[0], 10)
    objective.SetCoefficient(x[1], 15)
    objective.SetCoefficient(x[2], 20)
    objective.SetMinimization()
    
    #solve the system
    solver.Solve()
    opt_solution = 10 * x[0].solution_value() + 15 * x[1].solution_value() + 20 * x[2].solution_value()
    print('Number of variables =', solver.NumVariables())
    print('Number of constraints =', solver.NumConstraints())

    # The value of each variable in the solution.
    print('Solution:')
    for i in range(0,3):
        print('x = ', x[i].solution_value())

    # The objective value of the solution.
    print('Optimal objective value =', opt_solution)

algo()