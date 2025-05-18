"""
principal = 1000
annual_rate = 0.07 / 100
years = 10

amount = principal * (1 + annual_rate) ** years


for amount in range(1, 31):
  amount 
  


  print(f'{amount:,.2f}') 

"""
a = b = 7
print('a =', a, '\nb =', b)


for row in range(10):
 for column in range(10):
   print('<' if row % 2 == 1 else '>', end='')
 print()