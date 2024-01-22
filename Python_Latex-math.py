import math
import numpy as np
import latexify

latexify.__version__

def solve(a,b,c):
    return (-b+math.sqrt(b**2-4*a*c))/(2*a)
print(solve(1,4,3))
print(solve)

@latexify.function
def solve(a,b,c):
    return (-b+math.sqrt(b**2-4*a*c))/(2*a)
print(solve(1,4,3))
print(solve)
solve

@latexify.expression
def solve(a,b,c):
    return (-b+math.sqrt(b**2-4*a*c))/(2*a)
print(solve(1,4,3))
print(solve)
solve

@latexify.function
def sinc(x):
    if x==0:
        return 1
    else:
        return math.sin(x) /x
print(sinc)
sinc

@latexify.function(reduce_assignments=True, use_math_symbols=True)
def transform(x, y, a, b, theta, s, t):
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    scale = np.array([[a, 0, 0], [0, b, 0], [0, 0, 1]])
    rotate = np.array([[cos_t, -sin_t, 0], [sin_t, cos_t, 0], [0, 0, 1]])
    move = np.array([[1, 0, s],[0, 1, t], [0, 0, 1]])
    return move @ rotate @ scale @ np.array([[x], [y], [1]])
print(transform)
transform

@latexify.algorithmic
def collatz(x):
    n = 0
    while x > 1:
        n = n + 1
        if x % 2 == 0:
            x = x //2
        else:
            x = 3 *x + 1
    return n
print(collatz)
collatz

@latexify.get_latex
def greek(alpha, beta, gamma, Omega):
    return alpha * beta + math.gamma(gamma) + Omega
print(greek)
greek

