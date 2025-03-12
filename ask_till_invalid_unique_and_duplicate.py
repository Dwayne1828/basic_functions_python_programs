
#Asks til the user enters an invalid input
while True: 
    try:
        n = int(input("Enter a number: "))
    except ValueError:
        break
   