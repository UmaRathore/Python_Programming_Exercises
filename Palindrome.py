# check if a string is Palindrome

def checkPalindrome(input_string):
    if len(input_string) < 2:
        return True

    if input_string[0] == input_string[-1]:
        return checkPalindrome(input_string[1:-1])
    else:
        return False


status = checkPalindrome(" ")
print(status)
if status:
    print(f'string is Palindrome')
else:
    print(f'string is not Palindrome')
