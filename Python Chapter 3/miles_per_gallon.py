
total = 0
counter = 0 

while counter != -1:

	gallons_used = float(input('Enter the gallons used (-1 to end): '))
	miles_driven = int(input('Enter the miles driven: '))
	
	
	total = miles_driven / gallons_used
	print('The miles/gallons for this tank was: ', total)
	
	if counter == -1:
		break
average = total / counter 
	
print('The overall average miles/gallon was', average)	

	