#Creates an empty list to store the numbers
list_of_numbers = []

#Asks the user till input is invalid 
while True:
    try:
        number = int(input("Enter a number: "))
        list_of_numbers.append(number) #Adds the number to the list
    except ValueError:
        print("Invalid input")
        break
