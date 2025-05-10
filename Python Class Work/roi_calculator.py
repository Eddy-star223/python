amount = int(input('Enter amount: '))
years = int(input('Enter years: '))
interest_rate = int(input('Enter interest_rate: '))

interest_rate = interest_rate / 100
 
for number in range(1, years+1):
 
    return_roi = amount * (1 + interest_rate) ** number
    print(f'The return on investment {number} is {return_roi:.2f}')
  


