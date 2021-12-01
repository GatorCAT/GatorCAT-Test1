"""Summarize data values."""

from typing import List

import copy


def compute_mean(numbers: List[int]) -> float:
    """Compute mean for given list of integers."""
    # add a complete implementation of this function
    sum_of_num = sum(numbers)
    len_of_num = len(numbers)
    if numbers:
        return sum_of_num / len_of_num
    else:
        return float("nan")


def compute_median(numbers: List[int]) -> float:
    """Compute median for given list of integers."""
    # add a complete implementation of this function
    # sort the numbers in an "in place" fashion
    # after creating a "deep copy" of the numbers
    # array. Note that this is necessary because
    # it is not appropriate to sort the actual
    # list of numbers since this will potentially destroy
    # any other analysis or visualization done on list
    # Reference:
    # https://stackoverflow.com/questions/17873384/how-to-deep-copy-a-list
    if numbers:
        copy_numbers = copy.deepcopy(numbers)
        copy_numbers.sort()
        len_of_num = len(copy_numbers)
        # sort the numbers in an "in place" fashion
        if len_of_num % 2 == 0:
            mid1 = int(len_of_num / 2)
            mid2 = mid1 - 1
            med = compute_mean([copy_numbers[mid1], copy_numbers[mid2]])
            return med
        else:
            m = (len_of_num + 1) / 2
            m = int(m) - 1
            med = copy_numbers[m]
            return med
    else:
        return float("nan")


def compute_difference(numbers: List[int]) -> List[float]:
    """Compute difference for given lsit of integers."""
    # add a complete implementation of this function
    m = compute_mean(numbers)
    # compute the differences from the mean
    diff = []
    for num in numbers:
        diff.append(num - m)
    # return the computed differences from the mean
    return diff


def compute_variance(numbers: List[int]) -> float:
    """Compute variance for given list of integers."""
    # add a complete implementation of this function
    # compute the difference from the mean
    diff = compute_difference(numbers)
    # compute the squared differences
    squared_diff = []
    for d in diff:
        squared_diff.append(d ** 2)
    # calculate the variance
    sum_sqaured_diff = sum(squared_diff)
    variance = sum_sqaured_diff / len(numbers)
    # return the calculated variance of the list of numbers
    return variance


def compute_standard_deviation(numbers: List[int]) -> float:
    """Compute standard deviation for given list of integers."""
    # add a complete implementation of this function
    # call the function to calculate the variance
    variance = compute_variance(numbers)
    # calculate the standard deviation as the square root of the variance
    std = variance ** 0.5
    # return the calculated standard devision of the list of numbers
    return std
