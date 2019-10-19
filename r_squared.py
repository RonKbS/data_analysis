import numpy as np

def compute_r_squared(data, predictions):

    numerator = np.sum((data - predictions)**2)
    denominator = np.sum((data - np.mean(data))**2)
    r_squared = 1 - numerator / denominator

    return r_squared