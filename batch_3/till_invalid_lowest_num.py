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

#Fnction to find the lowest number
def lowest_number(list_of_numbers):
    lowest_num = min(list_of_numbers)
    return lowest_num

#Call the function and prints the result
lowest_num = lowest_number(list_of_numbers)
print("Lowest number: ", lowest_num)