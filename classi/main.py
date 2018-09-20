import sys 

from box import box
from cargo import cargo
#from V1_model import model
#from plotSolution import plotSolution
import random
import time

def main():
    packages =[]
    for i in range(0,3):
        w=120
        d=80
        packages.append(box([w,d]))
    camion =cargo([250,50])
    t=time.time()
    #s =model(packages,camion)
    #plotSolution(s,camion,packages)
    t=time.time()-t
    print(t)

if __name__ == "__main__":
    main()
