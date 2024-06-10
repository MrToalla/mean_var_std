import numpy as np

while True:
    user_digits = input("Please, enter 9 digits: ")
    if len(user_digits) == 9 and user_digits.isdigit():
        digit_list = []
        for digit in user_digits:
            digit_list.append(int(digit))
        break
    else:
        print("Invalid input, try again")


def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        digits_array = np.array(list).reshape((3, 3))
        arr_mean = array_mean(digits_array)
        arr_var = array_var(digits_array)
        arr_std = array_std(digits_array)
        arr_max = array_max(digits_array)
        arr_min = array_min(digits_array)
        arr_sum = array_sum(digits_array)
        calculations = {
            'mean': arr_mean,
            'variance': arr_var,
            'standard deviation': arr_std,
            'max': arr_max,
            'min': arr_min,
            'sum': arr_sum
        }

    return calculations


def array_mean(arr):
    axis1_mean = np.mean(arr, axis=0).tolist()
    axis2_mean = np.mean(arr, axis=1).tolist()
    flat_mean = np.mean(arr).tolist()
    mean_list = [axis1_mean, axis2_mean, flat_mean]
    return mean_list

def array_var(arr):
    axis1_var = np.var(arr, axis=0).tolist()
    axis2_var = np.var(arr, axis=1).tolist()
    flat_var = np.var(arr)
    var_list = [axis1_var, axis2_var, flat_var]
    return var_list

def array_std(arr):
    axis1_std = np.std(arr, axis=0).tolist()
    axis2_std = np.std(arr, axis=1).tolist()
    flat_std = np.std(arr)
    std_list = [axis1_std, axis2_std, flat_std]
    return std_list

def array_max(arr):
    axis1_max = np.max(arr, axis=0).tolist()
    axis2_max = np.max(arr, axis=1).tolist()
    flat_max = np.max(arr).tolist()
    max_list = [axis1_max, axis2_max, flat_max]
    return max_list

def array_min(arr):
    axis1_min = np.min(arr, axis=0).tolist()
    axis2_min = np.min(arr, axis=1).tolist()
    flat_min = np.min(arr).tolist()
    min_list = [axis1_min, axis2_min, flat_min]
    return min_list

def array_sum(arr):
    axis1_sum = np.sum(arr, axis=0).tolist()
    axis2_sum = np.sum(arr, axis=1).tolist()
    flat_sum = np.sum(arr).tolist()
    sum_list = [axis1_sum, axis2_sum, flat_sum]
    return sum_list


print(calculate(digit_list))