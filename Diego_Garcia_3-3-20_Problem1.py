#Function to calculate the standard deviation
def std_dev(numbers):
    sum = 0
    size = 0
    #Calculating the average
    for n in numbers:
        sum += float(n)
        size += 1
    average = sum/size
    sum = 0

    #Finding the sums of the squares
    for n in numbers:
        sum += (float(n) - average)**2

    dev = (sum/size)**(.5)
    return(dev)

#Getting the data set from the user, calling function, and printing results
num_lst = input('Please enter a list of numbers separated spaces: ')
num_lst = num_lst.split()
print(std_dev(num_lst))
