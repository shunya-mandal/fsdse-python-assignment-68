import numpy as np


def solution(array1, array2):
    """
    Enter your code here
    """
    array1, array2 = np.array(array1), np.array(array2)
    return np.concatenate((array1, array2.flatten()))
