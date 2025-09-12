smallest = None
largest = None
for num in [5, 3, 9]:
    if smallest is None or num < smallest:
        smallest = num
    if largest is None or num > largest:
        largest = num
print(smallest, largest)