
#Create a list to store the inputs
list_of_inputs = []

#Asks the user  till they enter an invalid input
while True:
    try:
        number = int(input("Enter a value: "))
        list_of_inputs.append(number)
    except ValueError:
        break

def average(list_of_inputs):
    #Calculate the average of the numbers
    average = sum(list_of_inputs) / len(list_of_inputs)
    return average

average_value = average(list_of_inputs)
print("Average: ", average_value)