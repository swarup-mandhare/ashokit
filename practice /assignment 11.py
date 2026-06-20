# Search for a number x in this tuple using loop:
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
i = 0
while i <len(tup):
    if (tup[i]==x ):
        print("Found at index", i)
    else:
        print ("Finding....")
    i += 1