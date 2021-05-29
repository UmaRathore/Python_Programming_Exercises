"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
nums = [1]
nums = [2,2,1]
nums = [4,1,2,1,2]
"""


# Solution - 2

import collections
nums = [2]
number_frequency = collections.Counter(nums)
for key, value in number_frequency.items():
    if value == 1:
        print(key)


# Solution - 1

# nums.sort()
#
# for i in range(len(nums)):
#     if i != 0 and nums[i] != nums[(len(nums)-1)] and nums[i] != nums[i+1]:
#         if nums[i+1] != nums[(len(nums)-1)] and nums[i+1] != nums[i+2]:
#             print(f'first : {nums[i+1]}')
#             break
#         if nums.index(nums[i+1]) == (len(nums) - 1):
#             print(f'third : {nums[i+1]}')
#             break
#     if i == 0 and nums[i] != nums[(len(nums)-1)] and nums[i] != nums[i+1]:
#         print(f'sec : {nums[i]}')
#         break
#     if i == 0 and nums[i] == nums[(len(nums) - 1)]:
#         print(f'four : {nums[i]}')
#         break

