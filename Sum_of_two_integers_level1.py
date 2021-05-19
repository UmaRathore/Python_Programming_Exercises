
# Given an array of integers nums and an integer target, return indices of the two numbers such
# that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(self, nums, target):
        sum_num = 0
        for i in range(len(nums)):
            if i != (len(nums)-1):
                j = i+1
                while j < len(nums):
                    sum_num = nums[j] + nums[i]
                    if sum_num == target:
                        return i, j
                    j += 1


test_array = [3, 3]
target_number = 6

sol1 = Solution(test_array, target_number)
print(sol1.twoSum(test_array, target_number))

