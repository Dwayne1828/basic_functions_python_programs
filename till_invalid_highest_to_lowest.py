
#Create a list to store the inputs
list_of_inputs = []

#Asks the user till they enter an invalid input
while True:
    try:
        number = int(input("Enter a value: "))
        list_of_inputs.append(number)
    except ValueError:
        break

#Create a function to sort the numbers from highest to lowest
def highest_to_lowest(list_of_inputs):
    list_of_inputs.sort(reverse=True)
    return list_of_inputs

high_to_low = highest_to_lowest(list_of_inputs)
print("Highest to lowest: ", high_to_low)