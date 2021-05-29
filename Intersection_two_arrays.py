"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must
appear as many times as it shows in both arrays and you may return the result in any order.
nums1=[1, 2, 2, 1] nums2=[2, 2]
nums1=[4, 9, 5] nums2=[9, 4, 9, 8, 4]

"""
import collections
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
limit = 0
result = []

nums_intersection_list = list(set(nums1) & set(nums2))
nums1_frequency = collections.Counter(nums1)
nums2_frequency = collections.Counter(nums2)

for item in nums_intersection_list:

    if nums1_frequency[item] > nums2_frequency[item]:
        limit = nums2_frequency[item]
    else:
        limit = nums1_frequency[item]

    i = 0
    while i < limit:
        result.append(item)
        i += 1

print(result)
