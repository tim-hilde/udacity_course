import turtle

def draw_square (some_turtle):
    for i in xrange (4):
        some_turtle.forward(100)
        some_turtle.right(90)
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #create turtle brad, draw square
    brad=turtle.Turtle()
    brad.hideturtle()
    brad.color("yellow")
    brad.speed(0)
    for i in xrange (36):
        draw_square(brad)
        brad.circle(100)
        brad.right(10)
    #create turtle angie, draw circle
    #angie=turtle.Turtle()
    #angie.hideturtle()
    #angie.color("blue")
    #angie.circle(100)

    window.exitonclick()

draw_art()
