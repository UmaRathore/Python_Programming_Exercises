# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320

def factorial(num):
    number_factorial = 1
    while num != 1:
        number_factorial = number_factorial*num
        num = num-1
    return number_factorial


print(factorial(8))
