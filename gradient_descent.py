import numpy
import pandas

def compute_cost(features, values, theta):

    m = len(values)
    sum_of_square_errors = numpy.square(numpy.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    
    cost_history = []

    for _ in range(num_iterations):
        predicted_values = numpy.dot(features, theta)
        theta = theta - alpha / len(values) * numpy.dot((predicted_values - values), features)
        cost_history.append(compute_cost(features, values, theta))

    return theta, pandas.Series(cost_history)
