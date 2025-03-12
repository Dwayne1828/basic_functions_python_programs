
list_of_numbers = [] #Creates an empty list to store the numbers

#Asks til the user enters an invalid input
while True: 
    try:
        number = int(input("Enter a number: "))
        list_of_numbers.append(number) #Adds the number
    except ValueError:
        break

#Function to check if the number is unique or duplicate
def unique_and_duplicate_numbers(list_of_numbers):
    if list_of_numbers.count(number) == 1:
        return "Unique"
    else:
        return "Duplicate"

#Call the function for the list and prints the result
unique_or_duplicate = unique_and_duplicate_numbers(list_of_numbers) 
print(unique_or_duplicate) 
