"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero
elements.Note that you must do this in-place without making a copy of the array.
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Input: nums = [0]
Output: [0]
"""

nums = [0, 0, 1]

count = 0
i = 0
array_limit = len(nums) - 1
while i < array_limit:
    if nums[i] == 0:
        nums.pop(i)
        count += 1
        array_limit = array_limit - 1
        i = 0
    else:
        i += 1

i = 0
while i < count:
    nums.append(0)
    i += 1

print(nums)
