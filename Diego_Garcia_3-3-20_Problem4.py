#Function to get the spacing and the x points we want to evaluated within the interval
def partition(lower, upper, amount, place = 'M'):
    step_size = (upper-lower)/amount
    steps = [lower]
    x_pts =[]

    #Itterates to create the spacing until it hits the upper bound
    while lower < upper:
        lower += step_size
        steps.append(lower)

    # Considers parameter of whether to take right or left of the intervals and defaults to middle if none is given
    if place == 'R':
        x_pts = steps[1:(amount+1)]
    elif place == 'L':
        x_pts = steps[0:amount]
    else:
        for x in steps[0:amount]:
            x_pts.append((x + step_size/2))

    #returning the list of the points we want to evaluate
    return x_pts

#Calculating the actual answer for our problem
answer  = (3/4)*(9)**4 - (3/4) - (4/3) * 9**3 + (4/3) + 1.6099 * 9**2 - 1.6099
print('We will integrate f(x) = 3x^3 - 4x^2 + 3.2198x from 1 to 9.')
print('Analytically we get F(x) = 3/4 x^4 - 4/3 x^3 + 1.6099 x^2. Which evaluates to :', answer)

#Defining the list with the amount of intervals we want to evaluate and initilizing lists for storage
N = [10, 50, 100, 200]
x_points = []
evaluation = []
for num in N:
    x_points.append(partition(1, 9, num))

#Tracker is used to get N to scale the sums according to the step size
tracker = -1
for points in x_points:
    tracker += 1
    sums = 0
    #Evaluates each list for each corresponding N
    for x in points:
        sums += (3*x**3 - 4 *x**2 + 3.2198*x)*8/N[tracker]
    evaluation.append(sums)

#Printing out the results of the evaluations
print('The approximation computed numerically for the each given N was as follows')
for x in range(4):
    print('N = '+ str(N[x]) + ' : Approx = ' + str(evaluation[x]))