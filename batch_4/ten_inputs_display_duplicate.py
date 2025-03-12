
#Create a list to store 10 inputs
list_of_inputs = [] 

#Create a loop to get 10 inputs from the user
for i in range(10):
    input_value = input("Enter a value: ")
    list_of_inputs.append(input_value)

def display_duplicate(list_of_inputs):
    #Create a list to store the duplicates
    duplicates = []
    
    for numbers in list_of_inputs:
        if list_of_inputs.count(numbers) > 1:
            duplicates.append(numbers) 
        return duplicates

#Call the function and store the result in a variable
duplicates = display_duplicate(list_of_inputs)
print(duplicates)
