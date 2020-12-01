from math import pi, e, sqrt, gcd, comb

def set_string(start, stop, step):
	return "{ " + f"{start}, {start + step}, ... , {stop}" + " }"

def sequence_string(sequence):
	l = len(sequence)
	string = "{ "
	for i in range(min(3, l)):
		string += f"{sequence[i]}, "
	if l > 3:
		string += " ... , "
		for i in range(max(-3, -l + min(3, l)), -1):
			string += f"{sequence[i]}, "
	return string[:-2] + " }"
	
def set_N(n):
	return set([x for x in range(0, n+1)]), set_string(0, n, 1)

def set_Z(n):
	return set([x for x in range(-n, n+1)]), set_string(-n, n, 1)

def set_Z_p(n):
	return set([x for x in range(1, n+1)]), set_string(1, n, 1)

def set_Z_n(n):
	return set([x for x in range(-n, 0)]), set_string(-n, -1, 1)

def ask_u():
	sets = {
		"N": set_N,
		"Z": set_Z,
		"Z_p": set_Z_p,
		"Z_n": set_Z_n,
	}
	while True:
		try:
			print("Sets:", ", ".join(sets.keys()))
			u = input("Assume the universal set: ")
			n = input("Up/down to n = ")
			return sets[u](int(n))
		except Exception as e:
			print("ERROR - try again.", e)

def ask_user():
	equation = input("We have the problem: ")
	variables = input("With variable(s): ").split(" ")
	return equation, variables

def main():
	true, false = [], []
	print("\n")
	set_u, set_u_string = ask_u()

	while True:
		try:
			equation, variables = ask_user()
			for_loop_recursive(variables, 0, set_u, [0] * len(variables), [equation, true, false])
			break
		except Exception as e:
			print("ERROR - try again.", e)
	
	print("\n" + equation + "\n")
	print(f"For {', '.join(variables)} € {set_u_string} :\n")
	
	if len(true[0]) == 2:
		reflexive, symmetric, transitive = True, True, True
		antisymmetric = 0
		for a in true:
			if not a[::-1] in true:
				if symmetric is True:
					symmetric = a[::-1]
				if type(antisymmetric) == int:
					antisymmetric += 1
			elif a[0] != a[1]:
				antisymmetric = [a, a[::-1]]
			elif type(antisymmetric) == int:
				antisymmetric += 1
			if reflexive is True:
				if not [a[0], a[0]] in true:
					reflexive = [a[0], a[0]]
			if transitive is True:
				for b in true:
					if a[1] == b[0] and not [a[0], b[1]] in true:
						transitive = [a, b]
						break
		
		print("Relation properties:")
		print(f"\tReflexive: {reflexive is True}")
		if not reflexive is True:
			print("\t\tWe do not have", reflexive)
		print(f"\tSymmetric: {symmetric is True}")
		if not symmetric is True:
			print("\t\tWe have", symmetric[::-1], ",\n\t\tbut not", symmetric)
		print(f"\tAntisymmetric: {type(antisymmetric) == int}")
		if type(antisymmetric) != int:
			print("\t\tWe have both", antisymmetric)
		print(f"\tTransitive: {transitive is True}")
		if not transitive is True:
			print("\t\tWe have both", transitive, ",\n\t\tbut not", str([transitive[0][0], transitive[1][1]]))
	
	d = [[[], []] for _ in variables]

	for v in range(len(variables)):
		for i in set_u:
			c = 0
			for t in true:
				c += (i == t[v])
			for f in false:
				c -= (i == f[v])
			l = len(set_u)
			if c == l:
				d[v][0].append(i)
			elif c == -l:
				d[v][1].append(i)
	print()
	for i in range(len(d)):
		if len(d[i][0]):
				print(f"Equation is true for all {variables[i]} = {sequence_string(d[i][0])}")
		if len(d[i][1]):
				print(f"Equation is false for all {variables[i]} = {sequence_string(d[i][1])}")
	
	dotdot = '\n\t\t...'
	print("\nThe equation is")
	print(f"\tTrue for {len(true)} cases,\n\t\t{' '.join([str(a) for a in (true[:4] + [dotdot] + true[-3:])])}.")
	print(f"\tFalse for {len(false)} cases,\n\t\t{' '.join([str(a) for a in (false[:4] + [dotdot] + false[-3:])])}.")

def for_loop_recursive(variables, index, set_u, values, final):
	if index != len(variables):
		for i in set_u:
			lst2 = values.copy()
			lst2[index] = i
			for_loop_recursive(variables, index+1, set_u, lst2, final)
	else:
		calculate(final[0], final[1], final[2], variables, values)

def calculate(equation, true, false, variables, values):
	for i in range(len(variables)):
		equation = equation.replace(variables[i], "(" + str(values[i]) + ")")

	try:
		if eval(equation):
			true.append(values)
		else:
			false.append(values)
	except Exception as e:
		print(f"Could not solve for {values}, because: {e}, in {equation}")

if __name__ == "__main__":
	main()
	