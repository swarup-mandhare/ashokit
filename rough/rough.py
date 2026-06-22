# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

lis = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
x = 48
i = 0
for el in lis:
    if (x == el):
        print ("Element found at inx : ",i)
    
    else:
        print("Element not found")   
    i += 1