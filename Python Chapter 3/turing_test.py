print('What is your problem?: ')
input() # ignore user input

while True:
  response = input('Have you had this problem before(yes or no): ').lower()
    
  if response == "yes":
    print('Well, you have it again.')

  elif response == "no":
    print('Well, you have it now')

  else:
    print('Invalid response. Enter yes or no')


  


