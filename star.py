import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen().bgcolor("black")
t.color("red")
t.speed(6)
t.width(4)
n = 66
h = 0

for i in range (5):
    t.right(144)
    for c in range (n):
        t.forward(3)
        c= colorsys.hsv_to_rgb(h,1,0.8)
        h += 1/n
        t.color(c)
turtle.exitonclick()