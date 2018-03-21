numbers = [value ** 3 for value in range(1, 11)]

for number in numbers:
    print(number)

print('The first three items in the list are:', numbers[:3])
print('Three items from the middle of the list are:', numbers[3:6])
print('The last three items in the list are:', numbers[-3:])
