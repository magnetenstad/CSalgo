
class Boo():
	def __init__(self, value) -> None:
		self.value = value

	# Types

	def __bool__(self):
		return self.value
	
	def __str__(self):
		return str(f"Boo({self.value})")
	
	def __int__(self):
		return int(self.value)

	def __float__(self):
		return float(self.value)

	# Binary operators

	# def __add__(self, other):
	# 	return int(self) + float(other)
	
	# def __sub__(self, other):
	# 	return int(self) - float(other)
	
	# def __mul__(self, other):
	# 	return int(self) * float(other)
	
	def __rshift__(self, other):
		return Boo((not self.value) or other.value)
	
	def __and__(self, other):
		return Boo(self.value and other.value)
	
	def __or__(self, other):
		return Boo(self.value or other.value)
	
	def __xor__(self, other):
		return Boo(self.value ^ other.value)
	
	# Comparison operators

	def __lt__(self, other):
		return Boo(self.value < other.value)

	def __gt__(self, other):
		return Boo(self.value > other.value)
	
	def __le__(self, other):
		return Boo(self.value <= other.value)

	def __ge__(self, other):
		return Boo(self.value >= other.value)
	
	def __eq__(self, other):
		return Boo(self.value == other.value)

	def __ne__(self, other):
		return Boo(self.value != other.value)

	# Unary operators

	def __invert__(self):
		return Boo(not self.value)
