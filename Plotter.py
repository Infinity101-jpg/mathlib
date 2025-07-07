### VARS ###

Units = 20;

### IMPORTS ###
import turtle


### FUNCTIONS ###
def init__screen():
  turtle.forward(0);

def runtime():
  while True:
    turtle.forward(0);
    turtle.update()

def draw__cartesian():
  turtle.forward(10 * Units);
  turtle.forward(-20 * Units);
  turtle.forward(10 * Units);
  turtle.left(90);
  turtle.forward(10 * Units);
  turtle.forward(-20 * Units);
  turtle.forward(10 * Units);

def plot(x,y):
  turtle.penup()
  turtle.forward(y * Units);
  turtle.right(90);
  turtle.penup()
  turtle.pencolor(1,0,0);
  turtle.forward(x * Units)
  turtle.pendown();
  turtle.forward(0.05 * Units)
  turtle.penup()
  turtle.home()
  turtle.left(0)
  


### BEGIN ###
def Plot(x,y):

  for item in x:

    turtle.hideturtle()
    turtle.tracer(0)

    init__screen()
    draw__cartesian()

    turtle.pensize(5)

    plot(item,y[ x.index(item) ])

  runtime()