# Q1. Find the sum of all numbers from 1 to n (user input).

# n = int(input("Enter the number n : "))
# sum = 0
# for i in range(1,n+1):
#     sum += i
#     i += 1
# print(sum)


# Q2. Search for a user-entered number in:
# n = int(input("Enter num to find : "))
# li  = [1,4,9,16,25,36,49,64,81,100]
# found = False 
# for i in li:
#     if n == i :
#         found = True
# if found:
#     print ("Found ")
# else :
#     print ("Not Found")

# no of time 7 apeared
# li = [7, 4, 7, 1, 7, 9, 7]
# a = 0
# for i in li:
#     if i==7 :
#         a+= 1
# print ("no of times 7 appeared is : ",a)

# largest no 
# li = [4, 8, 1, 99, 23, 17]
# largest = 0
# for i in li:
#     if (largest < i):
#         largest = i

# print(largest)

#smallest
# [4, 8, 1, 99, 23, 17]
# li = [4, 8, 1, 99, 23, 17]
# smallest = li[0]
# for i in li:
#     if (smallest > i):
#         smallest = i

# print(smallest)

li = [13, 8, 27, 42, 19, 64, 7, 50]
largest = 0
for i in li :
    if (i % 2 == 0):
        if (largest < i ):
            largest = i
print ("largest is : ", largest)




