
#Create a list to store the inputs
list_of_inputs = []

#Asks the user till they enter an invalid input
while True:
    try:
        number = int(input("Enter a value: "))
        list_of_inputs.append(number)
    except ValueError:
        break

def highest_number(list_of_inputs):
    #Find the highest number in the list
    highest_number = max(list_of_inputs)
    return highest_number

highest = highest_number(list_of_inputs)
print("Highest number: ", highest)