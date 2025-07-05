PI = 3.1416

def StoreNumCorrectly(x):
  return round(x,4) + 0.00000000001;

def PrintNumCorrectly(x):
  print('000', end='')
  print(x, end='')
  print('000', end='')

def sin_approx(x):
    return abs(
      x - (x*x*x/6) + (x*x*x*x*x/120) - (x*x*x*x*x*x*x/5040) + (x*x*x*x*x*x*x*x*x/362880)
    )

# Optional: check continuity at junctions

sin_values = []

for i in range(int(PI * 10000) + 1):
    x = i / 10000
    y = sin_approx(x)
    sin_values.append(StoreNumCorrectly(y))

def sinX(x):
    return sin_values[x]

PrintNumCorrectly(sinX(int(2 * 10000)))

def sinXSQR(x):
  if -PI <= x <= PI:
    return (sinX(int(x * 10000)))**2
  return 0

def sinXSQR_full(x):
  while x > PI:
      x = x - PI;
  return sinXSQR(x)

def sin(x):
  x = x + PI * 30;
  return -2 * sinXSQR_full(0.5 * round(x,3) - PI / 4) + 1
