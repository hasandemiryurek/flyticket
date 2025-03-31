import turtle

wn = turtle.Screen()
wn.bgcolor("black")
t = turtle.Turtle()
t.color("purple")
t.speed(1000)

def teleport(t, x, y):
    t.penup()
    t.setpos(x, y)
    t.pendown()

def vertical_line(t, l, s):
    t.pendown()
    t.left(90)
    t.forward(l)
    t.penup()
    t.forward(s+s)
    t.pendown()
    t.forward(l)
    t.penup()
    t.right(90)

def horizontal_line(t, l, s):
    t.pendown()
    t.left(90)
    t.forward(l)
    t.penup()
    t.forward(s)
    t.right(90)
    t.forward(s)
    t.pendown()
    t.forward(l)
    t.penup()

def letter_h(t, x, y, l, s, w):
    t.pensize(w)
    teleport(t,x,y)
    vertical_line(t,l,s)
    teleport(t,x,y)
    horizontal_line(t,l,s)
    teleport(t,x+l+s+s,y)
    vertical_line(t,l,s)

def letter_a(t, x, y, l, s, w):
    t.pensize(w)
    teleport(t, x, y)
    for i in range(2):
        horizontal_line(t, l, s)
        teleport(t, x, y+l+s+s)
    teleport(t, x+l+s+s, y)
    vertical_line(t, l, s)

def letter_s(t, x, y, l, s, w):
    t.pensize(w)
    teleport(t,x+s,y)
    t.forward(l-s)
    t.penup()
    t.forward(s)
    t.left(90)
    t.forward(s)
    t.pendown()
    t.forward(l)
    t.penup()
    t.forward(s)
    t.left(90)
    t.forward(s)
    t.pendown()
    t.forward(l-s)
    t.penup()
    t.forward(s)
    t.right(90)
    t.forward(s)
    t.pendown()
    t.forward(l-s)
    t.penup()
    t.forward(s)
    t.right(90)
    t.forward(s)
    t.pendown()
    t.forward(l-w)

def letter_n(t, x, y, l, s, w):
    t.pensize(w)
    teleport(t, x, y)
    vertical_line(t,l,s)
    teleport(t,x,y+l+s+l+s+s+s)
    t.right(50)
    t.penup()
    t.forward(s+s)
    t.pendown()
    t.forward(l+l/4)
    t.left(50)
    teleport(t,x+l+s,y)
    vertical_line(t,l,s)

def letter_d(t,x,y,l,s,w):
    t.pensize(w)
    teleport(t,x,y)
    vertical_line(t,l,s)
    teleport(t,x,y+l+l+2*s)
    t.right(45)
    t.penup()
    t.forward(s+s)
    t.pendown()
    t.forward(l+l/5)
    teleport(t,x,y)
    t.left(90)
    t.penup()
    t.forward(s+s)
    t.pendown()
    t.forward(l+l/5)


# t = turtle's name                           l= a length of a one piece of digital stick
# x = position of a turtle in x axis          s= space length after or before a one piece of digital stick
# y = position of a turtle in y axis          w= thickness of a turtle's pen


def hasnd(t, x, y, l, s, w):
     letter_h(t, x, y, l, s, w),letter_a(t, x+l+2*w+6*s, y, l, s, w),letter_s(t, x+2*l+5*w+10*s, y, l, s, w),letter_n(t, x+3*l+6*w+16*s, y, l, s, w),letter_d(t, x+4*l+8*w+21*s, y, l, s, w)

hasnd(t,-200,60,50,6,4)


t.hideturtle()
wn.exitonclick()

