import ezMaths as ez;

print('Pi is equal to ' + str(ez.Pi()))

print('The factorial of 9 is: ' + str(ez.Fact(9)))

print('Sin of Pi radians ' + str(
      ez.Sin(
        ez.Pi()
      )
      ))

print('Cos of Pi/3 Radians ' + str(
      ez.Cos(
        ez.Pi() / 3
      )
      ))

print('Tan of 1000 Radians ' + str(
      ez.Tan(
        1000
      )
      ))



x = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
y = [5,4,3,2,1,0,-1,-2,-3,-4,-5]

ez.PlotPoints (
  x, y
)
ez.ShowPlot()




x = -6;

for i in range(150):
  x = x + 0.1;
  y = x * x;
  try:
    ez.PlotPoints([x],[y])
  except Exception as Err:
    print(Err)

ez.ShowPlot()