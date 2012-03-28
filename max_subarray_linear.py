def find_max_subarray(A):
    return max_subarray_linear(A)

def max_subarray_linear(A):
    current_best_sum = 0
    current_best_start = -1
    current_best_end = -1

    new_start = 0
    new_sum = 0
    new_best_start = 0
    new_best_end = 0
    new_best_sum = 0

    for i in range(len(A)):
        new_sum += A[i]
        if A[i] > 0:
            new_best_sum = new_sum
            new_best_end = i
        if new_sum <= 0:
            new_start = i+1
            new_best_start = new_start
            new_sum = 0
            continue

# if the newest sum is good, replace the old sum and info
        if new_sum > current_best_sum:
            current_best_start = new_start
            current_best_end = i
            current_best_sum = new_sum

    return current_best_sum, current_best_start, current_best_end

if __name__ == "__main__":
    array = [-1, 4, 3, -1, -6, 3, -2, 3, 4]
    print find_max_subarray(array)
    
