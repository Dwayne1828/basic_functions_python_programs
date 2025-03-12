
#Asks the user for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#Check whose number is the smallest and biggest 
if num1 < num2:
#Using for loop that sets the range to what is inputted by the user 
    for i in range(num1 + 1, num2):
        print(i) #Prints the numbers between the two numbers

if num2 < num1:
    for i in range(num2 + 1, num1):
        print(i)

