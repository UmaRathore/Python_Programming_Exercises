# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320

def factorial(num):
    number_factorial = 1
    while num != 1:
        number_factorial = number_factorial*num
        num = num-1
    return number_factorial


while True:
    try:
        number_fact_list = {}
        total_numbers = int(float(input("How many number's factorial want to print : ")))
        if total_numbers > 0:
            for count in range(total_numbers):
                n = input("Enter number : ")
                number = int(n)
                if number > 0:
                    number_fact_list[n] = factorial(number)
                else:
                    print("Number should be greater than zero")

            print(number_fact_list)

        elif total_numbers < 0:
            print("No Factorial for negative integers")
    except ValueError:
        print("Enter integer greater than zero")
    else:
        print("Thank you")
        break
