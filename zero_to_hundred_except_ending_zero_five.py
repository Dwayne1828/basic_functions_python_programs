
#Using while loop to print all numbers from 0 to 100 except 5 and 50
count = 0
while count <= 100:
#Check if it is divisible by 5 which ends in 5 and 0 
    if count % 5 != 0:
        print(count)
    count += 1
