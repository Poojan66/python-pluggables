def max_subarray_sum(arr):
    """
    A function that finds the maximum subarray sum using Kadane's algorithm.

    Args:
        arr (list): A list of integers representing the array.

    Returns:
        The maximum subarray sum.
    """
    max_so_far = max_ending_here = 0
    for num in arr:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = max_subarray_sum(arr)
print(max_sum)
