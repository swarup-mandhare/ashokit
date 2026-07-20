#Take n as input and print the sum from 1 to n.

num = int(input("Enter the numbers to find the sum of : "))
sum = 0
for i in range(0, num) :
    sum += i
    i += 1
print (sum)