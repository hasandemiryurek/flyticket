import turtle

wn = turtle.Screen()
wn.bgcolor("black")
t = turtle.Turtle()
t.color("dodgerblue")
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
    teleport(t,x,y)
    t.forward(l)
    t.left(90)
    t.penup()
    t.forward(s)
    t.pendown()
    t.forward(l)
    t.penup()
    t.forward(s)
    t.pendown()
    t.left(90)
    t.forward(l)
    t.right(90)
    t.penup()
    t.forward(s)
    t.pendown()
    t.forward(l)
    t.right(90)
    t.penup()
    t.forward(s)
    t.pendown()
    t.forward(l-w)

def letter_n(t, x, y, l, s, w):
    t.pensize(w)
    teleport(t, x, y)
    vertical_line(t,l+3,s)
    teleport(t,x,y+l+s+l+s+s+s)
    t.right(50)
    t.penup()
    t.forward(s+s-2)
    t.pendown()
    t.forward(l+15)
    t.left(50)
    teleport(t,x+l+s,y)
    vertical_line(t,l+3,s)

def letter_d(t,x,y,l,s,w):
    t.pensize(w)
    teleport(t,x,y)
    vertical_line(t,l+3,s)
    teleport(t,x,y+l+l+20)
    t.right(45)
    t.penup()
    t.forward(s+s-4)
    t.pendown()
    t.forward(l+12)
    teleport(t,x,y)
    t.left(90)
    t.penup()
    t.forward(s+s-5)
    t.pendown()
    t.forward(l+14)

# t = turtle's name                           l= a length of a one piece of digital stick
# x = position of a turtle in x axis          s= space length after or before a one piece of digital stick
# y = position of a turtle in y axis          w= thickness of a turtle's pen









def hasnd(t, x, y, l, s, w):
     letter_h(t, x, y, l, s, w),letter_a(t, x+l+30, y, l, s, w),letter_s(t,x+l+l+60,y,l,s,w),letter_n(t,x+260,y,l,s,w),letter_d(t,x+345,y,l,s,w)

hasnd(t,-200,20,60,6,4)


