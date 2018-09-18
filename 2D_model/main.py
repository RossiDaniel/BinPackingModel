# some_file.py
from box import box
from cargo import cargo
from model import model2D
import random
import time

def main():
    packages =[]
    for i in range(0,7):
        w=(i%2)+1
        d=i+1
        packages.append(box([w,d]))
    packages.append(box([2,1]))
    camion =cargo([4,50])
    t=time.time()
    model2D(packages,camion)
    t=time.time()-t
    print(t)

if __name__ == "__main__":
    main()