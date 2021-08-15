# Pair Sums
# Given a list of n integers arr[0..(n-1)], d
# etermine the number of different pairs of elements within it which sum to k.
# If an integer appears in the list multiple times, each copy is considered to be different;
# that is, two pairs are considered different if one pair includes at least one array index which
# the other doesn't, even if they include the same values.

import math

# Add any extra import statements you may need here


# Add any helper functions you may need here
# 11:22
# 12:13

"""
Iteration o(n2)

ALGO
sum = 6

[1,2,3,4,3]

       [1,2,3,3,4]
sort : [1,2,3,3,4]

time : o(n) + log(n)

1: 3 = 4< 6 pass
2: 3 = 5 < 6
3: 3 = 6=6 [(3,3)]
3: 3 = 6=6 [(3,3),(3,3)]
4: 3 = 7 > 6 break

1) SORT LIST
2) For each item:
#       [1,2,3,3,4]
# sort : [1,2,3,3,4]


"""
# ==========================hash tables ==================================================

import math
# Add any extra import statements you may need here
import collections
import itertools


def combination_duplicates(key, repval):
    dpairs = 0
    itr = 0
    temp = []
    comb = []

    while itr < repval:
        temp.append(key)
        itr += 1

    comb = itertools.combinations(temp, 2)

    for i in comb:
        dpairs += 1

    return dpairs


def numberOfWays(arr, k):
    # Write your code here

    pairs = {}
    count = 0
    num = []
    key = 0
    dpairs = 0

    if len(arr) == 0:
        return

    frequency_items = collections.Counter(arr)

    for key, value in frequency_items.items():
        num.append(key)

    for element in num:
        key = (k - element)
        if key in frequency_items.keys():
            if frequency_items[key] == 1:
                count += 1
            else:
                repval = frequency_items[key]
                dpairs = combination_duplicates(key, repval)

    count = int(count / 2) + dpairs

    return count


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
    print('[', n, ']', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printInteger(expected)
        print(' Your output: ', end='')
        printInteger(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    k_1 = 6
    arr_1 = [1, 2, 3, 4, 3]
    expected_1 = 2
    output_1 = numberOfWays(arr_1, k_1)
    check(expected_1, output_1)

    k_2 = 6
    arr_2 = [1, 5, 3, 3, 3]
    expected_2 = 4
    output_2 = numberOfWays(arr_2, k_2)
    check(expected_2, output_2)

    # Add your own test cases here


# =======================  binary search method ===============================================

#
# def func_sum(arr, element, minval, maxval, k, count):
#     length = int((minval + maxval) / 2)
#
#     if length == 0:
#         return
#
#     if length == len(arr) - 1:
#         return
#
#     if element + arr[length] < k:
#         minval = length
#         maxval = len(arr)
#         func_sum(arr, element, minval, maxval, k, count)
#
#     elif element + arr[length] > k:
#         minval = 0
#         maxval = length
#         func_sum(arr, element, minval, maxval, k, count)
#
#     elif element + arr[length] == k:
#         print(arr[length])
#         count += 1
#
#     return count
#
#
# def numberOfWays(arr, k):
#     # Write your code here
#
#     count = 0
#
#     # half length of arr
#
#     if len(arr) is 0:
#         return
#
#     arr.sort()
#
#     for element in arr:
#         minval = 0
#         maxval = len(arr)
#         count = func_sum(arr, element, minval, maxval, k, count)
#
#     return count
#
#
# # These are the tests we use to determine if the solution is correct.
# # You can add your own at the bottom.
#
# def printInteger(n):
#     print('[', n, ']', sep='', end='')
#
#
# test_case_number = 1
#
#
# def check(expected, output):
#     global test_case_number
#     result = False
#     if expected == output:
#         result = True
#     rightTick = '\u2713'
#     wrongTick = '\u2717'
#     if result:
#         print(rightTick, 'Test #', test_case_number, sep='')
#     else:
#         print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
#         printInteger(expected)
#         print(' Your output: ', end='')
#         printInteger(output)
#         print()
#     test_case_number += 1
#
#
# if __name__ == "__main__":
#     k_1 = 6
#     arr_1 = [1, 2, 3, 4, 3]
#     expected_1 = 2
#     output_1 = numberOfWays(arr_1, k_1)
#     check(expected_1, output_1)
#
#     k_2 = 6
#     arr_2 = [1, 5, 3, 3, 3]
#     expected_2 = 4
#     output_2 = numberOfWays(arr_2, k_2)
#     check(expected_2, output_2)
#
#     # Add your own test cases here
