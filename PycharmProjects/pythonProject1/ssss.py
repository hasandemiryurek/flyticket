import turtle, random
wn = turtle.Screen()
track = turtle.Turtle()
track.speed(0)
track.penup()
track.setpos(-140,120)
track.pendown()

for i in range(15):
    track.write(i)
    track.penup()
    track.right(90)

    for j in range(8):
        track.forward(10)
        track.pendown()
        track.forward(10)
        track.penup()
    track.backward(160)
    track.left(90)
    track.forward(40)
track.hideturtle()

r = turtle.Turtle()
r.color("red")
r.shape("turtle")
r.penup()

a = turtle.Turtle()
a.color("black")
a.shape("turtle")
a.penup()

c = turtle.Turtle()
c.color("hot pink")
c.shape("turtle")
c.penup()

d = turtle.Turtle()
d.color("purple")
d.shape("turtle")
d.penup()

r.goto(-160,90)
a.goto(-160,50)
c.goto(-160,10)
d.goto(-160,-30)

for i in range(20):
    r.speed(random.randrange(0,6))
    a.speed(random.randrange(0,6))
    c.speed(random.randrange(0,6))
    d.speed(random.randrange(0,6))

    r.forward(30)
    a.forward(30)
    c.forward(30)
    d.forward(30)


wn.exitonclick()






