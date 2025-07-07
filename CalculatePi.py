
def factorial_iterative(n):
  if n < 0:
    return "Factorial is not defined for negative numbers."
  elif n == 0:
    return 1
  else:
    fact = 1
    for i in range(1, n + 1):
      fact *= i
  return fact

def sqrt (x):
  return x**0.5 ; 

def compute_pi_ramanujan(terms=5):
    total = 0
    factor = (2 * sqrt(2)) / 9801

    for n in range(terms):
        numerator = factorial_iterative(4 * n) * (1103 + 26390 * n)
        denominator = (factorial_iterative(n) ** 4) * (396 ** (4 * n))
        total += numerator / denominator

    return 1 / (factor * total)

pi = compute_pi_ramanujan(1000)

