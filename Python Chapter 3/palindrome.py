print('55555')

number = 55555 

first = (number / 10000) % 10
second = (number / 1000) % 10
third = (number / 100) % 10 
forth = (number / 10) % 10
fifth = number % 10

if first == fifth and second == forth:
  print('Is a palindrome')

else:
  print('Is not a palindrome')
  