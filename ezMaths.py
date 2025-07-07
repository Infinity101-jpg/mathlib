import CalculatePi
import CalculateSin
import Plotter
def Fact(x):
  return CalculatePi.factorial_iterative(x);

def Pi():
  return CalculatePi.pi;


DEGREES = ((1 / 180) * Pi())
RADIANS = 1 

def StoreNumCorrectly(x):
  return round(x,20) + 0.0000000000000001;

def PrintNumCorrectly(x):
  print('000', end='')
  print(x, end='')
  print('000', end='')

def sin_approx(x):
  return CalculateSin.taylor_sin(x);                                        #### Sin approx= Bhaskara I approximation

# Optional: check continuity at junctions

sin_values = []

for i in range(int(Pi() * 10000) + 1):
    x = i / 10000
    y = sin_approx(x)
    sin_values.append(StoreNumCorrectly(y))

def sinX(x):
    return sin_values[x]

def printNum(x):
   PrintNumCorrectly(StoreNumCorrectly(x))

def sinXSQR(x):
  if -Pi() <= x <= Pi():
    return (sinX(int(x * 10000)))**2
  return 0

def sinXSQR_full(x):
  while x > Pi():
      x = x - Pi();
  return sinXSQR(x)

def Sin(x):
  x = x + Pi() * 30;
  return -2 * sinXSQR_full(0.5 * round(x,3) - Pi() / 4) + 1

def Cos(x):
  return Sin(x + Pi() / 2)

def Tan(x):
  return Sin(x) / Cos(x);

def Degrees():
  return 1;

def Radians():
  return 180 / Pi();

def increment_list_elements(values):
    return [val + 0.00001 * (i + 1) for i, val in enumerate(values)]

def increment_list_elements_more(values):
    return [val + 0.001 * (i + 1) for i, val in enumerate(values)]


def Plot(x,y):
  return Plotter.Plot(increment_list_elements(x),increment_list_elements(y));

def PlotPoints(x,y):
  x_coords = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  y_coords = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]

  y_coords = y_coords + [0,0,0,0,0,0,0,0,0,0,0]
  x_coords = x_coords + [-5,-4,-3,-2,-1,0,1,2,3,4,5]

  x_coords = x_coords + increment_list_elements_more(x);
  y_coords = y_coords + increment_list_elements_more(y) ;

  Plot(x_coords, y_coords)

def ShowPlot():
  Plotter.y()

