
#Create a list to store the inputs
list_of_inputs = []

#Asks the user till they enter an invalid input
while True:
    try:
        number = int(input("Enter a value: "))
        list_of_inputs.append(number)
    except ValueError:
        break
