# some_file.py
from box import box
from cargo import cargo
from model import model2D
import random

def main():
    packages =[]
    for i in range(10):
        w=random.randint(1,2)
        d=random.randint(1,2)
        packages.append(box([w,d]))

    camion =cargo([3,10])
    model2D(packages,camion)

if __name__ == "__main__":
    main()