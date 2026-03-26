numbers = [100, 200, 300, 400]
print(numbers)
print(type(numbers))
print(numbers[0])
print(numbers[-2], numbers[3])   # negative and positive index accessing
print(numbers[0:3])              # slicing
print(numbers[-3:-1])            # negative slicing
print(numbers [:4])              # internally converts to [0:4]
for num in numbers:
    print(num)

#lists are mutable, hence
numbers[0]=1000
print("the new list is:",numbers)
numbers.append(500)
print(numbers)
numbers.sort()
print(numbers)
numbers.insert(1, 690)
print(numbers)