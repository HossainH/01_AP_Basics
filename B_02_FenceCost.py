#ask user for width and loop until they
#enter a number that is more than zero
from xml.sax.handler import feature_namespaces


def num_check():

    error = "Please enter numbers only" # in case user inputs letters

    while True:  #Infinite Loop (until values returned)
        try: #run code
            Length=float(input("Enter Length in meters")) #asks for Length
            Width = float(input("Enter Width in meters")) #asks for Width

            if Length > 0 and Width > 0: #check if values given are correct
                return Length, Width #if correct, then return those values which would end the def function

            elif Length < 0 or Width < 0: #checks if value is negative, which is invalid as area or perimeter can't be negative
                print("Length or Width can't be negative") #prints error message if
            else: # the only outcome left, is if the number is 0, so we don't use elif and use else directly
                print("Please enter a number that is more than zero")

        except ValueError: #except means that if this error happens, don't crash program and do this instead,
                            # in this case value error happens when user types letters instead of numbers
                print(error) #prints the appropriate error message

while True:
    CostOfFencing = float(input("Enter cost of fencing per meter"))
    if CostOfFencing == 0:
        print("Lucky you! getting it for free I see.")
        break
    elif CostOfFencing < 0:
        print("Please enter a valid cost")
    else:
        break

keep_going = ""

while keep_going == "":

    Length, Width= num_check() #uses the num check function to find the variables "width" and "height"

    print(f"width is {Width}") #prints the value returned by function
    print(f"length is {Length}") #prints the value returned by function


    perimeter = 2 * (Length + Width)

    print(f"the perimeter is {perimeter} meters")

    costoffencing= perimeter/CostOfFencing

    print(f"The cost of fencing your area is {costoffencing}")

    keep_going = input("Press enter key to use again, or press any key, then enter to stop")

print("Thanks for using our simple program")



