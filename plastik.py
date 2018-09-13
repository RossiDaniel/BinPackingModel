"""Linear optimization PLASTIK"""

from __future__ import print_function
from ortools.linear_solver import pywraplp

def main():
    # Istanzio Glop solver, naming it LinearExample.
    solver = pywraplp.Solver('LinearExample',
                            pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    #creo le variabili x1,x2,x3
    x1=solver.NumVar(0,solver.infinity(),'x1')
    x2=solver.NumVar(0,solver.infinity(),'x2')
    x3=solver.NumVar(0,solver.infinity(),'x3')
    
    #constraint 1: 2x1 + 2x2 + x3 >= 10000
    constraint1 = solver.Constraint(10000,solver.infinity())
    constraint1.SetCoefficient(x1,2)
    constraint1.SetCoefficient(x2,2)
    constraint1.SetCoefficient(x3,1)

    #constraint 2: 2x1 + 3x2 + 2x3 >= 180000
    constraint2 = solver.Constraint(180000,solver.infinity())
    constraint2.SetCoefficient(x1,2)
    constraint2.SetCoefficient(x2,3)
    constraint2.SetCoefficient(x3,2)

    #constraint 3: x1 + x2 + 5x3 >= 20000
    constraint3 = solver.Constraint(20000,solver.infinity())
    constraint3.SetCoefficient(x1,1)
    constraint3.SetCoefficient(x2,1)
    constraint3.SetCoefficient(x3,5)

    # Objective function: .
    objective = solver.Objective()
    objective.SetCoefficient(x1, 10)
    objective.SetCoefficient(x2, 15)
    objective.SetCoefficient(x3, 20)
    objective.SetMinimization()
    
    #solve the system
    solver.Solve()
    opt_solution = 10 * x1.solution_value() + 15 * x2.solution_value() + 20 * x3.solution_value()
    print('Number of variables =', solver.NumVariables())
    print('Number of constraints =', solver.NumConstraints())

    # The value of each variable in the solution.
    print('Solution:')
    print('x1 = ', x1.solution_value())
    print('x2 = ', x2.solution_value())
    print('x3 = ', x3.solution_value())

    # The objective value of the solution.
    print('Optimal objective value =', opt_solution)
if __name__ == '__main__':
  main()