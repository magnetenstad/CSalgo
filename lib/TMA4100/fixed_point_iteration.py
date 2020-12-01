from math import *
from ..lib import *

def fixed_point_iteration(f, x0, N):
	x = [x0]
	for i in range(N):
		x.append(compute(f, [("x", x[i])]))
	return x

def print_result(x):
	try:
		print("\nResult:")
		for i, xi in enumerate(x):
			print(f"{i: >4d}: {xi:.4f}")
	except Exception as e:
		print(f"ERROR - {e}")

def main():
	f, x0, N = ask(("f", "x0", "N"), types=(str, float, int))
	x = fixed_point_iteration(f, x0, N)
	print_result(x)

if __name__ == "__main__":
	main()
