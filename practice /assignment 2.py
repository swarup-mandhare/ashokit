# Take a number from user.
# Check:
# * Even or Odd
# * Positive, Negative or Zero

# Enter number: -8

# Even
# Negative

num = int(input("Enter your number : "))
if ((num%2)==0):
    print("Number is Even")
else :
    print("Number is Odd")

if (num > 0):
    print("Number is Positive")
else :
    print("Number is Negative")
