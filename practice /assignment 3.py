# Take a name as input and print:

# * Original name
# * Total number of characters
# * First character
# * Last character

name = input("Enter your name :")
count = len(name)
print("Your original name is : ")
print("Total number of charecters in your name are : ",count)
print("First character of your name is",name[0])
print("Last character of your name is",name[-1])