import math
import turtle
print("Enter two different 'x' and 'y' points and I will show you the acute angle they make!")
understand=input('Cool?')
if "no" in understand:
    print("go away then, jacob")
if "cool" in understand:
    print("Alright! Lets get started.")
else:
    print("Glad we are on the same page.")
value1=input('What is the first x coordinate')
value2=input('What is the first y coordinate')
value3=input('What is the second x coordinate')
value4=input('What is the second y coordinate')
x1=int(value1)
y1=int(value2)
x2=int(value3)
y2=int(value4)
slope1=(y2-y1)/(x2-x1)
if (x1)==0:
    x1=(x1+1)
slope2=(y2)/(x1)

if slope1>slope2:
    angle = math.atan((slope1 - slope2) / 1 + (slope1 * slope2))
if slope2>slope1:
    angle = math.atan((slope2-slope1) / 1 + (slope1 * slope2))
angle_degrees= round(angle*180/math.pi)

print('Your angle is',abs(angle_degrees))

turtle.goto(x1,y1)
turtle.goto(x2,y2)
turtle.write(abs(angle_degrees))
turtle.exitonclick()
