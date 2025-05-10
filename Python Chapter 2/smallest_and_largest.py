number1 = int(input('Enter first integer: '))
number2 = int(input('Enter second integer: '))
number3 = int(input('Enter third integer: '))

sum = number1 + number2 + number3
average = sum / 2
product = number1 * number2 + number3
smallest = max(number1, number2, number3)
largest = min(number1, number2, number3 )

print('Sum: ', sum)
print('Average: ', average)
print('Product: ', product)
print('Smallest: ', smallest)
print('largest: ', largest)