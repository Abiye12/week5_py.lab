#allows the user to type a number
number = input("Enter a number: ")

#Stores the variable "number" as an integer
number = int(number)

#prints the string below
print("The numbered entered was", number)

#checks if the number is divisible by 2 i.e if its an odd number
if (number % 2) == 0:
	print("That is an even number")
elif number % 10 == 0:
        print("it is a multiple of 10")
else:
	print("That is an odd number")
