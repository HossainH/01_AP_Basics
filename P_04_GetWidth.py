#ask user for width and loop until they
#enter a number that is more than zero
def num_check():

    error = "Please enter numbers only" # in case user inputs letters

    while True:  #Infinite Loop (until values returned)
        try: #run code
            width=float(input("Enter width")) #asks for width
            height = float(input("Enter height")) #asks for height

            if width > 0 and height > 0: #check if values given are correct
                return width, height #if correct, then return those values which would end the def function

            elif width < 0 or height < 0: #checks if value is negative, which is invalid as area or perimeter can't be negative
                print("width or height can't be negative") #prints error message if
            else: # the only outcome left, is if the number is 0, so we don't use elif and use else directly
                print("Please enter a number that is more than zero")

        except ValueError: #except means that if this error happens, don't crash program and do this instead,
                            # in this case value error happens when user types letters instead of numbers
                print(error) #prints the appropriate error message

width, height= num_check() #uses the num check function to find the variables "width" and "height"

print(f"width is {width}") #prints the value returned by function
print(f"height is {height}") #prints the value returned by function

