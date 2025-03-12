
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
    count_dict = {} #Create a dictionary to store the count of each number
    for number in list_of_inputs:
        count_dict[number] = list_of_inputs.count(number)
    
    #Find the number with the highest count in the dictionary items
    for key, value in count_dict.items():
        if value == max(count_dict.values()):
            return key, value 

max_duplicate, count = most_duplicate(list_of_inputs)
print("Most duplicate: ", max_duplicate, "Count: ", count)