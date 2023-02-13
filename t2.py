from turtle import*

pencolor('blue')
pensize(3)
fillcolor('red')
speed('fastest')
for i in range(10,0,-1):
    begin_fill()
    circle(i*100)
    lt(255)
    end_fill()
mainloop()    

