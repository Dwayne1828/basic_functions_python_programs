
#Asks the user for 10 numbers using a loop
#Starts the counter at 0
even_counter = 0

for i in range(10):
    num = int(input("Enter a number: ")) 
    #Checks if the number is even
    if num % 2 == 0:
        even_counter += 1 #Iterate even_counter by 1  

#Print the number of even numbers
print(even_counter)
