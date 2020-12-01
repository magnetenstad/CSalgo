from math import gcd, prod

def collect_congruenses():
	a, m = [], []
	n = int(input("\nHow many congruence equations do you have? "))
	for i in range(1, n+1):
		ai, mi = input(f"What is a{i} and m{i}? ").split(" ")
		a.append(int(ai))
		m.append(int(mi))
	return a, m

def is_relatively_prime(m):
	l = len(m)
	for i in range(l):
		for j in range(i+1, l):
			if gcd(m[i], m[j]) != 1:
				return False
	return True

def mod_inverse(a, m):
	a = a % m
	for x in range(1, m):
		if ((a * x) % m == 1):
			return x
	return 1

def get_inverses(a, M):
	return [mod_inverse(a[i], M[i]) for i in range(len(a))]

def get_M(m):
	Mt = prod(m)
	M = [Mt / mm for mm in m]
	return Mt, M

def print_i(i, a, m, inverse, M):
	print(f"a{i}: {a}, m{i}: {m}, M{i}: {M}, y{i}: {inverse}")

def main():
	a, m = collect_congruenses()
	print()
	if is_relatively_prime(m):
		Mt, M = get_M(m)
		y = get_inverses(M, m)
		l = len(a)
		for i in range(l):
			print_i(i+1, a[i], m[i], y[i], M[i])
		print()
		x = 0
		print("x = ")
		for i in range(l):
			x += a[i]*M[i]*y[i]
			print(f"+ {a[i]} * {M[i]} * {y[i]}")
		print(f"( mod {Mt} )")
		print(f"  = {x} ( mod {Mt} )\n")
		print(f"x = {x % Mt} ( mod {Mt} )")
	else:
		print("m's are not relatively prime,\n the chinese remainder theorem can't be applied.")

if __name__ == "__main__":
	main()
	