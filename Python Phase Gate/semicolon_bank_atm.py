def bank_atm():
        account_balance = account_balance
        balance = 50.000


def account_balance(amount):
	if amount == 50.000:
		balance += amount
	print(f"Your current balance: {balance:.2f}")

def withdrawal(amount):
	if (balance % 500) != 0:
		print('Cannot withdraw more than 90%')

	elif balance < 1000:
		print('Invalid')
	
	elif balance > 1000: 
		print('Transaction succesful')
		print(f" withdrawal Amount: {balance:.2f}")

	charge = 100
	balance -= amount - charge
	
	print(f" Withdrawal Fee {charge}") 
	remaining_balnce = balance
	
							 
	print(f"remaining_balance: {remaining_balance:.2f}")
	
def main():
    bank_atm = bank_atm()
    while True:
        print('Welcome to Semicolon Bank ATM')
        print("1. Account Balance")
        print("2. Withdrawal")
       	user = input("Choose an option: ")

	if user == "1":
		account_balance = double(input('Enter your account balance: '))
		bank_atm.account_balance(account_number)
	
	else if user == "2":
		withdrawal = double(input('Enter withdrawal amount multiples of 500 0r 1000: '))
		bank_atm.withdrawal(withdrawal)

	

