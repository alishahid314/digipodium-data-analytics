from turtle import *

speed('fastest')
pencolor('red')
fillcolor('blue')

for i in range (5):
    fd (100)
    for i in range(5):
        fd(50)
        for i in range(5):
            fd(50)
            lt(72)
        lt(72)
    rt(72) 

hideturtle()
mainloop()