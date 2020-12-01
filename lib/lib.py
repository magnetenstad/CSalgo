
def calculate(func, variables):
	try:
		for name, value in variables:
			func = func.replace(name, f"({value})")
		return eval(func)
	except Exception as e:
		print(f"\nERROR - {e}")
