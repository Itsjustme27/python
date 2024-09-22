
# Collatz Sequence

def collatz(number):
	if number%2 == 0:
		return number // 2
	elif number%2 != 0:
		return 3 * number + 1
	else:
		return 0
try:
	numLoop = True
	while numLoop:
		num = int(input("Enter an integer: "))
		print(collatz(num))
		if collatz(num) == 1:
			print("Output 1 detected! Exiting program!")
			numLoop = False
except:
	print("Error! Please enter a valid Integer!")




