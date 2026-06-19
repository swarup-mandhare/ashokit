# Assignment 5: Marks Checker
# Take marks as input.
# Print:
# * Distinction (>=75)
# * First Class (>=60)
# * Pass (>=35)
# * Fail (<35)

marks = float(input("Enter you percentage: "))
if (marks<35):
    print("You failed the exams")
elif (marks<=60):
    print("You passed the exams")
elif (marks <= 75):
    print("You passed the exam with first class")
else:
    print("You passed the exam with distinction")