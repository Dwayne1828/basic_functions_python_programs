
#Asks the user for 10 numbers
#Creates an empty list to store the numbers
input_list = [] 

for i in range(10):
    number = int(input("Enter a number: "))
    if number not in input_list:
        input_list.append(number) #Adds the number to the list
    
print(input_list) #Prints the list of numbers that are not duplicates
