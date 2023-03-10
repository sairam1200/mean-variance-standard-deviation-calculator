import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.array(lst).reshape(3, 3)
    mean = [np.mean(arr, axis=i) for i in range(3)]
    variance = [np.var(arr, axis=i) for i in range(3)]
    std_dev = [np.std(arr, axis=i) for i in range(3)]
    max_val = [np.max(arr, axis=i) for i in range(3)]
    min_val = [np.min(arr, axis=i) for i in range(3)]
    sum_val = [np.sum(arr, axis=i) for i in range(3)]
    return {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_val,
        'min': min_val,
        'sum': sum_val
    }
