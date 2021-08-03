
# Math and Stats: Calculate the power of a number
# Given a double, x, and an integer, n, write a function to calculate x raised to the power n. For example:
#
# power(2, 5) = 32
# power(3, 4) = 81
# power(1.5, 3) = 3.375
# power(2, -2) = 0.25

class PowerNumber:

    def __init__(self, x, n):
        self.x = x
        self.n = n
        self.result = 0

    def func_power(self, x, n):
        if self.x == 0:
            return 0

        if self.n == 0:
            return 1

        while self.n > 0:
            self.n = self.n-1
            self.result = self.x * self.func_power(x, n)

        return self.result


output = PowerNumber(2, 5)
print(output.func_power(2, 5))
