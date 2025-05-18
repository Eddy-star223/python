number = int(input('Enter number'))


factorial = 1
for number in range(number, 1, -1):
  factorial *= number

print(factorial)

