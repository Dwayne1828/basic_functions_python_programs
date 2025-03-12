
input_list = [] #Creates an empty list to store the numbers

#Asks the users for 10 numbers 
for i in range(10):
    number = int(input("Enter a number: "))
    input_list.append(number) #Adds the number to the list

#Creates a new empty list to store the numbers that are not duplicates
no_duplicate_list = []

#Counts how many times each number appears in the list 
for num in input_list:
    if input_list.count(num) == 1: 
        no_duplicate_list.append(num)

print(no_duplicate_list) 


