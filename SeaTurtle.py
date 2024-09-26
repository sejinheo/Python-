import turtle as t

def draw_star():
    for _ in range(5):
        t.forward(100)
        t.right(144)


t.shape("turtle")
t.speed(3) 
t.color("yellow") 


t.penup()
t.goto(-200, 100)
t.pendown()
draw_star()


t.penup()
t.goto(0, 100)
t.pendown()
draw_star()


t.penup()
t.goto(200, 100)
t.pendown()
draw_star()


t.penup()
t.goto(-100, -100)
t.pendown()
draw_star()


t.penup()
t.goto(100, -100)
t.pendown()
draw_star()

t.hideturtle() 
t.done()  
