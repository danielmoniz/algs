from datetime import datetime
from math import floor
import random
import max_subarray as alg1
import max_subarray_naive as alg2
import max_subarray_linear as linear

def compare_subarray_algs():
    num_tests = 5
    sample_range = [i - int(floor(num_tests / 2)) for i in range(num_tests)]
    print "sample range:", sample_range
    input_sizes = [i**4 for i in range(1, num_tests)]
    victor = []

    for i in range(len(input_sizes)):
        input_size = input_sizes[i]
        array = [random.choice(sample_range) for i in range(input_size)]
        # array = random.sample(sample_range, input_size)
        
        alg1_start = datetime.now()
        alg1.sort(array)
        alg1_time = datetime.now() - alg1_start 

        alg2_start = datetime.now()
        alg2.sort(array)
        alg2_time = datetime.now() - alg2_start 

        print alg1_time, alg2_time
        if alg1_time < alg2_time:
            victor.append(("D&C", input_size, alg1_time))
        else:
            victor.append(("naive", input_size, alg2_time))

    print victor



num_tests = 5
sample_range = [i - int(floor(num_tests / 2)) for i in range(num_tests)]
array = [random.choice(sample_range) for i in range(10000)]

array = [-1, 4, 3, -1, -6, 3, -2, 3, 4]

print linear.sort(array)
