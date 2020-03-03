#Opening the data file
file = open('random_x_y_pairs.txt','r')
print('Opening the file and begining to process the selected data.')

#Initializing the values to be used in the calculation and in the loops
x_avg = 0
y_avg = 0
n = 0
expected_value = 0
x_std_dev = 0
y_std_dev = 0
XY = []

#Calculating the sums and the XY list
for line in file:
    n += 1
    line = line.split()
    x_avg += float(line[0])
    y_avg += float(line[1])
    XY.append(float(line[0]) * float(line[1]))

file.close()

#Calculatinf the expected value and averages
for num in XY:
    expected_value += num/n
x_avg = x_avg/n
y_avg = y_avg/n

#Had to close and reopen file in order to iterate over the file once more
file = open('random_x_y_pairs.txt','r')
for line in file:
    line = line.split()
    x_std_dev += (float(line[0]) - x_avg)**2
    y_std_dev += (float(line[1]) - y_avg)**2

file.close()

#Calculating the standard deviations
x_std_dev = (x_std_dev/n)**(0.5)
y_std_dev = (y_std_dev/n)**(0.5)

#Printing the results of the calculations
print('Calculation done  ...\nThe linear correlation coefficient from this data set is:', (expected_value-x_avg*y_avg)/(x_std_dev*y_std_dev))