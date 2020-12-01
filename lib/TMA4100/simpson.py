from ..lib import *
from math import sin, cos, e, pi
from numpy import *


# Function from TMA4100 Wiki

def simpson(f, a, b, m=10):
	# Find an approximation to an integral by the composite Simpson's method:
	# Input:
	#   f:    integrand
	#   a, b: integration interval
	#   2*m:  number of subintervals
	# Output: The approximation to the integral
	n = 2*m
	x_noder = linspace(a, b, n+1)       # equidistributed nodes from a to b
	h = (b-a)/n                         # stepsize
	S1 = f(x_noder[0]) + f(x_noder[n])  # S1 = f(x_0)+f(x_n)
	S2 = sum(f(x_noder[1:n:2]))         # S2 = f(x_1)+f(x_3)+...+f(x_{n-1})
	S3 = sum(f(x_noder[2:n-1:2]))       # S3 = f(x_2)+f(x_4)+...+f(x_{n-2})
	S = h*(S1 + 4*S2 + 2*S3)/3
	return S


def simpson_analog(f, a, b, N):
	X = linspace(a, b, N+1)
	h = (b - a) / N
	S, S_str, Y_str, F_str = [], [], [], []

	coefficients = [1] + [(2 + 2 * (i % 2)) for i in range(1, N)] + [1]
	
	for i, x in enumerate(X):
		fx = compute(f, [("x", x)])
		S.append(fx * coefficients[i])
		S_str.append(str(coefficients[i]) + "*" + str(round(fx, 4)))
		Y_str.append(str(coefficients[i]) + "*y_" + str(i))
		F_str.append(str(coefficients[i]) + "*f(" + str(x) + ")")
	s = sum(S)
	print(f"\nValues\n\t(a, b):\t ({a}, {b})\n\t2n:\t {N}\n\th:\t = (b - a) / 2n = {h}\n")
	print(f"\nS_{N}\t= (h/3) * (" + " + ".join(Y_str) + ")")
	print(f"\n\t= (h/3) * (" + " + ".join(F_str) + ")")
	print(f"\n\t= (h/3) * (" + " + ".join(S_str) + ")")
	print(f"\n\t= ({h}/3) * ({round(s, 4)})")
	print(f"\n\t= {round(h*s/3, 4)}")

def main():
	f, a, b, n = ask(("f", "a", "b", "2n"), (str, int, int, int))
	simpson_analog(f, a, b, n)

if __name__ == "__main__":
	main()
