"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range
that is missing from the array.
Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
Test cases:
nums = [3,0,1]
nums = [0,1]
nums = [9,6,4,2,3,5,7,0,1]
nums = [0]

"""

nums = [9,6,4,2,3,5,7,0,1]
nums.sort()

i = 0
while i <= len(nums):
    nums.index(i)
    if i not in nums:
        print(f'number : {i}  not present in nums')

    i += 1
