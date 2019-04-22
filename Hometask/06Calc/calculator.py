

class Calculator:
	def multiply(self, a, b):
		result = a * b
		return result

	def add(self, a, b):
		result = a + b
		return result

#---------------------------------

calc = Calculator()

result_1 = calc.add(111, 10)
print(result_1)

result_2 = calc.multiply(2, 100)
print(result_2)
