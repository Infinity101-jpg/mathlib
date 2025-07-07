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
  turtle.forward(12 * Units);
  turtle.forward(-24 * Units);
  turtle.forward(12 * Units);
  turtle.left(90);
  turtle.forward(10 * Units);
  turtle.forward(-20 * Units);
  turtle.forward(10 * Units);

def plot(x,y):
  turtle.penup()
  turtle.forward(y * Units);
  turtle.right(90);
  turtle.penup()
  if -0.001 <= x <= 0.001 and -11 <= y <= 11:
    turtle.pencolor(1,0,0);
  else:
    if -0.001 <= y <= 0.001 and -12 <= x <= 13:
      turtle.pencolor(1,0,0);
    else:
      pass;
  turtle.forward(x * Units)
  turtle.pendown();
  turtle.forward(0.05 * Units)
  turtle.penup()
  turtle.home()
  turtle.left(0)
  
def erase__cartesian () :
  turtle.home();
  turtle.pencolor(1,1,1);
  turtle.penup ();
  turtle.forward(10.3 * Units)

  turtle.pendown()
  turtle.forward(10000 * Units);
  turtle.backward(10000 * Units)

  turtle.penup()
  turtle.backward(10.3 * Units)

  turtle.backward(10.3 * Units);
  turtle.pendown()
  turtle.backward ( 100000)
  turtle.forward(   100000)
  turtle.penup()
  turtle.forward(10.3 * Units)

### BEGIN ###
def Plot(x,y):
  for item in x:
    turtle.hideturtle()
    turtle.tracer(0)

    init__screen()
    draw__cartesian()
    erase__cartesian()

    turtle.pensize(5)
    turtle.left(90)
    if -5.1 <= item <= 5.1 and -5.1 <= y[ int(x.index(item)) ] <= 5.1:
      turtle.pencolor(0,0,1)
    else:
      turtle.pencolor(1,1,1)
    plot((item*2) ,y[ int(x.index(item)) ]*2)

def y():
  runtime()