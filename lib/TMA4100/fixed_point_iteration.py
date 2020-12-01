from math import *
from ..lib import *

def ask_for_values():
	while True:
		try:
			f = input("\nA function f(x) for x: ")
			x0 = float(input("A value for x0: "))
			N = int(input("Iteration count N: "))
			return f, x0, N
		except:
			print("ERROR - try again.")

def fixed_point_iteration(f, x0, N):
	x = [x0]
	for i in range(N):
		x.append(calculate(f, [("x", x[i])]))
	return x

def print_result(x):
	try:
		print("\nResult:")
		for i, xi in enumerate(x):
			print(f"{i: >4d}: {xi:.4f}")
	except Exception as e:
		print(f"ERROR - {e}")

def main():
	f, x0, N = ask_for_values()
	x = fixed_point_iteration(f, x0, N)
	print_result(x)

if __name__ == "__main__":
	main()
