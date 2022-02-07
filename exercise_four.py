#  return should number of integers that are between the sets
from functools import reduce
from math import gcd


def getTotalX(a, b):
    lcm_a = reduce(lambda x, y: x * y // gcd(x, y), a)
    gcd_b = reduce(gcd, b)
    print(sum(1 for x in range(lcm_a, gcd_b + 1, lcm_a) if gcd_b % x == 0))
    return sum(1 for x in range(lcm_a, gcd_b + 1, lcm_a) if gcd_b % x == 0)


number_elements_arrays = input('Enter number of elements in arrays a and b with space:').rstrip().split()

number_elements_first_arr = int(number_elements_arrays[0])
number_elements_second_arr = int(number_elements_arrays[1])

arr = list(map(int, input('Enter item of first set:').rstrip().split()))
brr = list(map(int, input('Enter item of second set:').rstrip().split()))

total = getTotalX(arr, brr)

