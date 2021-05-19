# Write a function that reverses a string. The input string is given as an array of characters s.

from json import dumps


class Solution:
    @staticmethod
    def reverse_string(s):
        s.reverse()
        print(dumps(s))


string_name = ["h", "e", "l", "l", "o"]
Solution.reverse_string(string_name)
