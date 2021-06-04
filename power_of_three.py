"""
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3powerx.

"""

n = 45
status = ''

if n == 1:
    status = True
elif n == 0:
    status = False
else:
    if n % 3 == 0:
        while n > 1:
            n = n / 3
            if n == 1:
                status = True
                break
            elif n < 1:
                status = False
    else:
        status = False


print(status)

