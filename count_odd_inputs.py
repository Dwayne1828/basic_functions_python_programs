#Initialized odd to 0
odd = 0

#Asks the user for values ten times
for i in range(10): 
    num = int(input("Enter a number: "))
    #If the number is odd, increment odd by 1
    if num % 2 != 0:
        odd += 1

#Prints the total number of odd numbers
print(odd)