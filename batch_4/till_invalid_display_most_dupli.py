
#Create a list to store the inputs 
list_of_inputs = []

#Asks the user till they enter an invalid input
while True:
    try:
        number = int(input("Enter a value: "))
        list_of_inputs.append(number)
    except ValueError:
        break

def most_duplicate(list_of_inputs):
    
    count_dict = {}
    
    for number in list_of_inputs:
        count_dict[number] = list_of_inputs.count(number)
    
    return count_dict

count = (most_duplicate(list_of_inputs))
print(count)   