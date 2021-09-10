import turtle

turtle.title("Fractal tree")        #changes the title of the TurtleScreen
turtle.bgcolor("black")             #changes the background color of the TurtleScreen

a=turtle.Turtle()       #initializes a variable 'a', which we use throughout the program to refer to turtle
a.lt(90)                #the turtle rotates 90 degrees to the left (start position > after 90 degrees ^)
a.shape("turtle")       #changes the shape of the turtle ("turtle","circle" etc.)
a.shapesize(0.8)        #increase or decrease the size of the onscreen turtle
a.pencolor("blue")      #changes the outline color of the turtle
a.fillcolor("black")    #changes the fill color of the turtle
a.speed("fastest")      #speed of our turtle cursor

#call the tree function inside the tree frunction
def tree(num): 
    while num>10:
        a.fd(num)       #the turtle moves forward (60 pixel)
        a.lt(30)        #turns 30 degrees to the left
        tree(4*num/5)
        a.rt(60)        #turns 60 degrees to the right      
        tree(4*num/5)
        a.lt(30)        #turns 30 degrees to the left
        a.bk(num)       #the turtle moves backwards by distance
        return

tree(60)
#stop execution
turtle.done()