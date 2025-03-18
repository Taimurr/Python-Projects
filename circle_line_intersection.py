# CPSC 231 LO1 Spring 2020
# Taimur Rizwan
# UCID: 30078941
# This code is used to take an input for printing various sizes of a circle and line and calculate the points where they intersect 



import turtle
import math



WIDTH = 800
HEIGHT = 600
MIDDLEX = WIDTH/2
MIDDLEY = HEIGHT/2
SMALLCIRCRAD = 5

#window size

screen = turtle.getscreen()
screen.setup(800,600,0,0)
screen.setworldcoordinates(0,0,800,600)
turtle.hideturtle()

#axis
turtle.penup()
turtle.goto(MIDDLEX,0)
turtle.pendown()
turtle.goto(MIDDLEX,600)

turtle.penup()
turtle.goto(0,MIDDLEY)
turtle.pendown()
turtle.goto(800,MIDDLEY)

#input for circle
turtle.penup()

xc = int(input("Please enter the x coordinate for your circle: "))
yc = int(input("Please enter the y coordinate for your circle: "))
crad = float(input("Please enter the radius of your circle: "))

x1 = int(input("Please enter the x coordinate for the starting line: "))
y1 = int(input("Please enter the y coordinate for the starting line: "))

x2 = int(input("Please enter the x coordinate for the ending line: "))
y2 = int(input("Please enter the y coordinate for the ending line: "))

turtle.color("red")

turtle.goto(xc,yc-crad)
turtle.pendown()
turtle.circle(crad)

#Drawing the line
turtle.penup()

turtle.color("blue")
turtle.goto(x1,y1)

turtle.pendown()

turtle.goto(x2,y2)

turtle.penup()
#calculates the points where the line will intersect the circle

a = ((x2-x1)**2) + ((y2-y1)**2)
b = 2*((x1-xc)*(x2-x1) + (y1-yc)*(y2-y1))
c = ((x1-xc)**2) + ((y1-yc)**2) - ((crad)**2)

#for when there are no intersections
if (b**2) - 4*(a*c) < 0:
    turtle.goto(MIDDLEX,MIDDLEY)
    turtle.color("green")
    turtle.write("No intersections")
#for when there is 1 intersection in an infinite line 
if (b**2) - 4*(a*c) == 0:
    alph1 = (-b)/(2*a)
    if (alph1 >= 0) and (alph1 <= 1): 
        intx1 = ((1-alph1)*x1) + (alph1*x2)
        inty1 = ((1-alph1)*y1) + (alph1*y2)
        
        #This is where I draw my circle for instersection with the real line
        turtle.goto(intx1,inty1 - SMALLCIRCRAD)
        turtle.color("green")
        turtle.pendown()
        turtle.circle(SMALLCIRCRAD)
        turtle.penup()
        print("1 intersection")
        print("is at (", intx1,",", inty1, ")")
    else:
        turtle.goto(MIDDLEX,MIDDLEY)
        turtle.color("green")
        turtle.write("No intersections")
        
#for when there are 2 intersections in an infinite line        
if (b**2) - 4*(a*c) > 0:
    disc1 = math.sqrt((b**2) - 4*(a*c))
    alph1 = (-b+disc1)/(2*a)
    alph2 = (-b-disc1)/(2*a)

    intx1 = ((1-alph1)*x1) + (alph1*x2)
    inty1 = ((1-alph1)*y1) + (alph1*y2)

    intx2 = ((1-alph2)*x1) + (alph2*x2)
    inty2 = ((1-alph2)*y1) + (alph2*y2)

    #when there are 2 real intersections
    if ((alph1 >= 0) and (alph1 <= 1)) and ((alph2 >= 0) and (alph2 <= 1)):
    
        turtle.goto(intx1,inty1 - SMALLCIRCRAD)
        turtle.color("green")
        turtle.pendown()
        turtle.circle(SMALLCIRCRAD)
        turtle.penup()

        turtle.goto(intx2,inty2 - SMALLCIRCRAD)
        turtle.color("green")
        turtle.pendown()
        turtle.circle(SMALLCIRCRAD)
        turtle.penup()
        print("2 intersections")
        print("is at (", intx1,",", inty1, ") and at (", intx2,",", inty2, ")")

    #When the first point is a real intersection but not the second
    elif (alph1 >= 0) and (alph1 <= 1):
        turtle.goto(intx1,inty1 - SMALLCIRCRAD)
        turtle.color("green")
        turtle.pendown()
        turtle.circle(SMALLCIRCRAD)
        turtle.penup()
        print("1 intersection")
        print("is at (", intx1,",", inty1, ")")

    #When the second point is a real intersection but not the second
    elif (alph2 >= 0) and (alph2 <= 1):
        turtle.goto(intx2,inty2 - SMALLCIRCRAD)
        turtle.color("green")
        turtle.pendown()
        turtle.circle(SMALLCIRCRAD)
        turtle.penup()
        print("1 intersection")
        print("is at (", intx2,",", inty2, ")")
    #When there are no real intersections
              
    else:
        turtle.goto(MIDDLEX,MIDDLEY)
        turtle.color("green")
        turtle.write("No intersections")
