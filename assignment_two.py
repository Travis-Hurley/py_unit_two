import math
import turtle
value1=input('What is the first x coordinate')
value2=input('What is the first y coordinate')
value3=input('What is the second x coordinate')
value4=input('What is the second y coordinate')
x1=int(value1)
y1=int(value2)
x2=int(value3)
y2=int(value4)
slope1=(y2-y1)/(x2-x1)
slope2=(y1-0)/(x1-0)
angle=math.atan((slope2-slope1)/1+(slope1*slope2))
angle_degrees= angle*180/math.pi
9
print(abs(angle_degrees))

turtle.goto(x1,y1)
turtle.goto(x2,y2)

turtle.exitonclick()
