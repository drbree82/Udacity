import turtle

#Make a window
window = turtle.Screen()
window.bgcolor("red")

def draw_square():


#Turtle call
    brad = turtle.Turtle()
    brad.shape("square")
#Loop to create square
    for x in range(0,4):
        brad.forward(100)
        brad.right(90)
        
draw_square()

#Turtle Call    
def draw_circle():
    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("green")
#Draw Circle
    angie.circle(100)

draw_circle()

#Quit at finish
window.exitonclick()
