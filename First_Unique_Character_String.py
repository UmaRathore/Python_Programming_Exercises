"""
Given a string s, return the first non-repeating character in it and return its index.
If it does not exist, return -1.
s = 'leetcode'
s = 'loveleetcode'
s = 'aabbcdcdk'
s = 'aabb'
"""

# Solution 2

import collections

s = 'aabbcdcdk'
status = ""
frequencies = collections.Counter(s)
repeated = {}

for key, value in frequencies.items():
    if value == 1:
        repeated[key] = value
        status = 'Unique value exist'
        print(f'{status} : {repeated} at index {s.find(key)}')
        break
    else:
        status = 'No Unique Values'

if status == 'No Unique Values':
    print(f'{status} : -1')


# Solution - 1

# s = 'aabb'
# repeat_value = ""
# status = ""
# i = 0
# while i < len(s):
#     count = 0
#     j = i + 1
#     while j < len(s):
#         if s[i] == s[j]:
#             repeat_value = repeat_value + s[i]
#             count += 1
#             break
#         j += 1
#     if count == 0 and repeat_value.find(s[i]) == -1:
#         print(f'index of unique character {i}')
#         status = "success"
#         break
#     elif count == 0 and repeat_value.find(s[i]) != -1:
#         status = "failure"
#     i += 1
#
# if status == "failure":
#     print(f'there is no unique character : -1')
