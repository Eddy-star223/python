def multiply(number1, number2):
	total = 0
	for number in range(0, number2):
		total += number1
	if number2 < 0:
		total -= total
	return total

print(multiply(2, 4))
print(multiply(5, 4))
print(multiply(77, -4))
	
 