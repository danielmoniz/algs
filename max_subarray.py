from math import floor
import max_subarray_naive as naive

def find_max_crossing_subarray(A, low, mid, high):
    """linear-time algorithm to determine the largest summed subarray that 
    crosses the middle line of the divide and conquer algorithm."""
    print "In find_max_crossing_subarray"
    left_sum = -float("inf");
    sum = 0
    for i in reversed(range(mid+1)):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    
    right_sum = -float("inf");
    sum = 0
    for j in range(mid+1, high+1):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

# return the dimensions and size of the subarray
    return max_left, max_right, left_sum + right_sum

def find_max_subarray(A, low, high):
    if low == high:
        return low, high, A[low]
    elif high - low <= 20000:
        print "directing to naive algorithm..."
        return naive.find_max_subarray(A, low, high)
    else:
        print "using standard algorithm..."
        mid = int(floor((low + high) / 2))
        left_low, left_high, left_sum = find_max_subarray(A, low, mid)
        right_low, right_high, right_sum = find_max_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum
        

def sort(array):
    find_max_subarray(array, 0, len(array)-1)
    max_left, max_right, subarray_sum = find_max_subarray(array, 0, len(array)-1)

    return array
