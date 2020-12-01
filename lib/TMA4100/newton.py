from math import atan, sin, cos

def newton(f, df, x0, tol=1.e-8, max_iter=30):
	# Solve f(x)=0 by Newtons method
	# The output of each iteration is printed
	# Input:
	#   f, df:   The function f and its derivate f'.
	#   x0:  Initial values
	#   tol: The tolerance
	# Output:
	#   The root and the number of iterations
	x = x0
	print('k ={:3d}, x = {:18.15f}, f(x) = {:10.3e}'.format(0, x, f(x)))
	k1 = 0
	for k in range(max_iter):
		k1 = k + 1
		fx = f(x)
		if abs(fx) < tol:           # Accept the solution 
			break 
		x = x - fx/df(x)            # Newton iteration
		print('k ={:3d}, x = {:18.15f}, f(x) = {:10.3e}'.format(k1, x, f(x)))
	return x, k1

def newton_analog(f, df, x0, n, show_fx=False):
	x = x0
	print(f"\nx_0\t= {x}\nf(x_0)\t= {f(x):10.3e}\n")
	for k in range(n):
		fx = f(x)
		dfx = df(x)
		x_next = x - fx / dfx
		print(f"x_{k+1}\t= x_{k} - f(x_{k}) / df(x_{k})\n\t= {x:.4f} - ({fx:.4f} / {dfx:.4f})\n\t= {x_next:.4f}")
		print(f"f(x_{k+1})\t= {f(x_next):10.3e}\n" * show_fx)
		x = x_next
	return x

# Example 2
"""
def f(x):                   # The function f
	return atan(x) - 2*x + 4

def df(x):                  # The derivative f'
	return 1 / (x**2 + 1) - 2

x0 = 2          # Starting value
x = newton_analog(f, df, x0, 3)  # Apply Newton
"""
# x, nit = newton(f, df, x0, tol=1.e-10, max_iter=30)  # Apply Newton
# print('\n\nResult:\nx={}, number of iterations={}'.format(x, nit))

def main():
	pass

if __name__ == "__main__":
	main()
