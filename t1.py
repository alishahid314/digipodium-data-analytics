from turtle import *

speed('fastest')

side = 10
size = 50

#create a hexagon
for i in range(size):
    forward(size)
    left(360/side)
    write(i)

hideturtle()
mainloop()
