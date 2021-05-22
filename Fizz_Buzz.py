# Given an integer n, return a string array answer (1-indexed) where:
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i if non of the above conditions are true.


import json


class Solution:

    @staticmethod
    def fizzBuzz(n):
        answer = []
        i = 1
        while i <= n:
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
            i = i+1
        return answer


given_numbers = 15

temp_variable = Solution.fizzBuzz(given_numbers)
print(json.dumps(temp_variable))
