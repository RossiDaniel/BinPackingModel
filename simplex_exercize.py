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
    
    #constraint 1: -x1 + 4x2 - 2x3 <= 8
    constraint1 = solver.Constraint(-solver.infinity(),8)
    constraint1.SetCoefficient(x1,-1)
    constraint1.SetCoefficient(x2,4)
    constraint1.SetCoefficient(x3,-2)

    #constraint 2: x1 + x2 +2x3 <= 12
    constraint2 = solver.Constraint(-solver.infinity(), 12)
    constraint2.SetCoefficient(x1,1)
    constraint2.SetCoefficient(x2,1)
    constraint2.SetCoefficient(x3,2)

    # Objective function: .
    objective = solver.Objective()
    objective.SetCoefficient(x1, 5)
    objective.SetCoefficient(x2, -2)
    objective.SetCoefficient(x3, -3)
    objective.SetMinimization()
    
    #solve the system
    solver.Solve()
    opt_solution = 5 * x1.solution_value() -2 * x2.solution_value() -3 * x3.solution_value()
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