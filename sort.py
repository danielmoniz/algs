from datetime import datetime
from math import floor
import random
import max_subarray as alg1
import max_subarray_naive as alg2

num_tests = 15
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
