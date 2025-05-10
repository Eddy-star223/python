

purchase = int(input('Enter amount: '))

if purchase >= 1000 and purchase <= 10000:
  discount = purchase * 0.05
  total = purchase - discount
  discount = purchase * (5 /100)
  print('The discount is: ', discount)
  print(f'The total amount is {total:,.2}')
 

elif purchase >= 10000 and purchase <= 50000:
  discount = purchase * 0.10
  total = purchase - discount
  print('The discount is: ', discount)
  print(f'The total amount is {total:,.2f}')
  
elif purchase > 50000:
  discount = purchase * 0.20
  total = purchase - discount
  discount = purchase * (20 / 100)
  print('The discount is: ', discount)
  print(f'The total amount is {total:,.2f}')
  

else:
	print(Invalid)