
sum_remaining = 0

#Asks the user for 10 numbers using a loop
for i in range(10): 
    num = int(input("Enter a number: "))

#Store the first number in a variable and the sum of remaining 
    if i == 0:
        first_num = num
    else:
        sum_remaining += num

#Solve for the difference of the first number and the sum of the remaining numbers
difference = first_num - sum_remaining

#Print the difference 
print(difference)
    
