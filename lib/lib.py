
def compute(func, variables):
	try:
		for name, value in variables:
			func = func.replace(name, f"({value})")
		return eval(func)
	except Exception as e:
		print(f"\nERROR - {e}")

def ask(questions, types=None):
	while True:
		try:
			if types == None:
				return [input(f"{q}: ") for q in questions]
			else:
				return [types[i](input(f"<{types[i].__name__}> {q}: ")) for i, q in enumerate(questions)]
		except Exception as e:
			print(f"ERROR - {e}")
