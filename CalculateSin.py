import CalculatePi

def taylor_sin(x, terms=10):
    sine_approx = 0
    x = x 
    for n in range(terms):
        numerator = (-1)**n * x**(2*n + 1)
        denominator = CalculatePi.factorial_iterative(2*n + 1)
        sine_approx += numerator / denominator
    return sine_approx


