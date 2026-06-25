# # Take n as user input and print the sum from 1 to n
# # num = int(input("Enter the number to find sum till : "))
# # sum = 0
# # for i in range (0, num+1):
# #     sum += i
# # print(sum)

# # search a number in list 
# # num = int(input("Enter the num to find : "))
# # found = False
# # li = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# # for i in li:
# #     if num == i:
# #        found = True
# # if found:
# #     print ("found")
# # else :
# #     print ("Not found")

# # # Count how many times 7 appears in:
# # li = [7, 4, 7, 1, 7, 9, 7]
# # x = 0
# # for i in li :
# #     if i == 7:
# #         x += 1
# # print ("The number of times 7 occoured is : ", x)

# #Find the largest number in:
# # li = [4, 8, 1, 99, 23, 17]
# # largest = li[0]
# # for i in li :
# #     if i > largest :
# #         largest = i
# # print (largest)

# # #Find the smallest number in:
# # li = [4, 8, 1, 99, 23, 17]
# # smallest = li[0]
# # for i in li :
# #     if i < smallest :
# #         smallest = i
# # print (smallest)

#Find the largest even number in:
li = [13, 8, 27, 42, 19, 64, 7, 50]
largest = None
for i in li :
    if (i % 2 == 0):
        if largest == None or i > largest  :
            largest = i
print ("largest even among all is :", largest )

# #Take n as user input and print its factorial.

# # num = int(input("Enter the number to find factorial of : "))
# # fac = 1
# # for i in range (1, num+1):
# #     fac *= i
# #     i += 1
# # print ("Factorial of number is : ",fac)

# Print numbers from 1 to 100.

# * Multiple of 3 → Fizz
# * Multiple of 5 → Buzz
# * Multiple of both → FizzBuzz
# * Otherwise print the number.

# for i in range (1, 101):
#     if (i % 3 == 0 and i % 5 == 0 ):
#         print ("FizzBuzz")
#     elif (i % 3 == 0):
#         print ("Fizz")
#     elif (i % 5 == 0):
#         print ("Buzz")
#     else:
#         print (i )
