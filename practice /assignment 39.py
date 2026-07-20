# # #Take n as input and print the sum from 1 to n.

# # num = int(input("Enter the number till which youu want to find sum : "))
# # sum = 0
# # for i in range (0,num+1):
# #     sum += i
# # print (sum)

# # li = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# # num = int(input("Enter the number to find : "))
# # found = False
# # for i in (li):
# #     if num == i :
# #         found = True
# # if found :
# #     print ("Found")
# # else :
# #     print ("Not found")

# # count = 0
# # li = [7, 4, 7, 1, 7, 9, 7]
# # for i in li:
# #     if i == 7:
# #         count += 1
# # print (count)

# li = [4, 8, 1, 99, 23, 17]
# largest = None
# for i in li:
#     if largest is None or i >= largest :
#         largest = i
# print (largest)

# li = [4, 8, 1, 99, 23, 17]
# smallest = None
# for i in li:
#     if smallest is None or i <= smallest :
#         smallest = i
# print (smallest)

# li = [13, 8, 27, 42, 19, 64, 7, 50]
# largest = None
# for i in li :
#     if (i % 2 == 0):
#         if largest is None or i >= largest :
#             largest = i
# print (largest)

# # Take a number n as user input and print its factorial.
# num = int(input("Enter a number to find factorial of : "))
# fac = 1
# for i in range (1, num +1):
#     fac *= i
# print (fac)

# Print numbers from 1 to 100.

# Rules:

# * Multiple of 3 → Fizz
# * Multiple of 5 → Buzz
# * Multiple of both 3 and 5 → FizzBuzz
# * Otherwise print the number.

for i in range (0,101):
    if (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif (i % 3 == 0):
        print ("Fizz")
    elif (i % 5 == 0):
        print ("Buzz")
    else :
        print (i)
