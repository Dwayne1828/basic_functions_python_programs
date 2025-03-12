
#Asks the user till input is invalid
#Creates an empty list to store the numbers
list_of_numbers = []

while True:
    try:
        number = int(input("Enter a number: "))
        list_of_numbers.append(number) #Adds the number to the list
    except ValueError:
        print("Invalid input")
        break

#Function to sort the numbers from lowest to highest
def lowest_to_highest(list_of_numbers):
    list_of_numbers.sort()
    return list_of_numbers 

#Call the function and prints the result
sorted_list = lowest_to_highest(list_of_numbers)
print("Sorted list: ", sorted_list)