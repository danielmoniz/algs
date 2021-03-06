def sort(A):
    return find_max_subarray(A, 0, len(A) - 1)

def find_max_subarray(A, low, high):
    total_best_sum = -float("inf")
    total_best_start = -1
    total_best_end = -1

    for i in range(high):
        best_sum = 0
        best_end = 0
        current_sum = 0

        for j in range(i, high):
            current_sum += A[j]
            if current_sum > best_sum:
                best_end = j
                best_sum = current_sum


        if best_sum > total_best_sum:
            total_best_sum = best_sum
            total_best_start = i
            total_best_end = best_end

    if total_best_sum < 0:
        return -1, -1, 0
    return total_best_start, total_best_end, total_best_sum
