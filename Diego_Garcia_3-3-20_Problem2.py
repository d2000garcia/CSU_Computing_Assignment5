#Obtaining the list of numbers
numbers = input('Please enter a list of numbers separated spaces: ')
numbers = numbers.split()

#Initializing values and dictionary to be used in loop
#Dictionary uses numbers in data set as keys and the number of occurances as the value
print('Begining sorting process . . .')
amount = {}
min = 1000000000000
max = -1000000000000
for n in numbers:
    if float(n) < min:
        min = float(n)
    if float(n) > max:
        max = float(n)
    if float(n) in numbers:
        amount[float(n)] += 1
    else:
        amount[float(n)] = 1

#Initializing the list to store the sorted numbers iterate in steps of one until hiting the max
sorted_list = []
min += -1
while min < max:
    min += 1
    if min in amount:
        for n in range(amount[min]):
            sorted_list.append(min)

#Printing the sorted list
print('Now the sorted list is ready\n')
print(sorted_list)