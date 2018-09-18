import turtle

def quadrato(T,l):
    for i in range(4):
        T.fd(l)
        T.lt(90)
    turtle.mainloop()

def poligono(T,n):
    for i in range(n):
        T.fd(100)
        T.lt(360/n)
    turtle.mainloop()

bob = turtle.Turtle()
#quadrato(bob,200)
poligono(bob,16)