integer = int(input('Enter binary number(only 0 and 1): '))

decimal = 0
position = 0

while integer > 0:
  digit = integer % 10
  decimal = digit * (2 ** position)
  integer //=10
  position += 1

print('Decimal equivalent: ', decimal)
  