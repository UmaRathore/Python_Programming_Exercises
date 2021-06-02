"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
nums = [1,2,3,1]
nums = [1,2,3,4]
nums = [1,1,1,3,3,4,3,2,4,2]
"""

import collections

nums = [1,2,3,4]
number_frequency = collections.Counter(nums)
count = 1

for key, value in number_frequency.items():
    print(value)
    if value > 1:
        count += 1

if count > 1:
    print("true")
else:
    print("false")
