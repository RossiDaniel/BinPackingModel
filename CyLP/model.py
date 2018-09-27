import numpy as np
from cylp.py.modeling.CyLPModel import CyLPArray
from cylp.cy import CyClpSimplex
s = CyClpSimplex()

# Add variables
x = s.addVariable('x', 3)
y = s.addVariable('y', 2)

# Create coefficients and bounds
A = np.matrix([[1., 2., 0],[1., 0, 1.]])
B = np.matrix([[1., 0, 0], [0, 0, 1.]])
D = np.matrix([[1., 2.],[0, 1]])
a = CyLPArray([5, 2.5])
b = CyLPArray([4.2, 3])
x_u= CyLPArray([2., 3.5])

