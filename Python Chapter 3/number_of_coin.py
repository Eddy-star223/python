price = float(input("Enter purchase price (<= 500): "))
while price < 0 or price > 1:
    price = float(input("Invalid input. Enter purchase price (<= 1.00): "))

change = round((1.00 - price) * 100) 

quarters = change // 25
change %= 25

dimes = change // 10
change %= 10

pennies = change

print("Your change is:")
print(f"{quarters} quarter")
print(f"{dimes} dime")
print(f"{pennies} pennies")






