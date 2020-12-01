from math import pi, e, sqrt
from .boo import Boo
from math import gcd, comb

VARIABLES = {}

def interpret(string):
	for key, value in VARIABLES.items():
		string = string.replace(key, str(value))
	
	return string

def truth_table():
	print("\nSyntax:\n\tand: '&' / 'and'\n\tor: '|' / 'or'\n\tnot: '~' / 'not'\n\tconditional: '->'\n\tbiconditional: '<->'\n")
	proposition = input("Give proposition: ")
	variables = input("Give variables: ").split(" ")
	print()

	l = len(variables)
	
	proposition = proposition.replace("and", " & ")
	proposition = proposition.replace("or", " | ")
	proposition = proposition.replace("not", " ~ ")
	proposition = proposition.replace("<->", " == ")
	proposition = proposition.replace("->", " >> ")
	proposition = proposition.replace("!", " not ")

	header = []
	for variable in variables:
		header.append(variable)
	header.append("#")
	header.append(proposition.replace(" ", ""))

	for i, variable in enumerate(variables):
		name = "_" + variable + "_"
		proposition = proposition.replace(variable, name)
		variables[i] = name

	table = []

	for i in range(2**l):
		bit_string = format(i, "b").zfill(l)
		
		table.append([])
		for j, variable in enumerate(variables):
			value = bool(int(bit_string[j]))
			VARIABLES[variable] = Boo(value)
			table[i].append(["F", "T"][value])
		table[i].append("|")

		interpretation = interpret(proposition)
		table[i].append(["F", "T"][bool(eval(interpretation))])
		# except:
		# 	print("ERROR - Proposition is invalid.")
	VARIABLES.clear()

	return table, header

def print_table(table, header):
	header_string = ""
	for el in header:
		header_string += el + " "
	print(header_string)
	sep = "-"*len(header_string)
	for i in range(len(header_string)):
		if header_string[i] == "#":
			sep = sep[:i] + "|" + sep[i+1:]
	print(sep)
	for row in table:
		for i, el in enumerate(row):
			print(el.center(len(header[i])), end=" ")
		print("\n"+sep)

def main():
	table, header = truth_table()
	print_table(table, header)

if __name__ == "__main__":
	main()
	