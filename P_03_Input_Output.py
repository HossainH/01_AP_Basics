#ask the user for their name

name=str(input("What is your name?"))
print()

#ask the user for their favorite integer

number=int(input("What is your favorite number? We will half, double and square it for you!"))
print()

#Greet the user
print(f"Hello {name}! You have chosen the number {number}, that's pretty cool! thanks for using our service")
print()

# double, half and square their favorite integer
double = number*2
half = number*0.5
square = number**2

#Output the results
print(f"After some magic, we found out that {number} doubled is {double}, {number} halved is {half} and lastly, {number} squared is {square}")