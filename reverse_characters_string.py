# Strings: Reverse words in a sentence
# Reverse the order of words in a given sentence (an array of characters).
# Take the “Hello World” string for example:

# Time complexity = O(n)
# Space complexity = O(n)

def reverse_character_string(given_string):

    length_str = len(given_string)

    if length_str == 0:
        return

    output_string_local = given_string[::-1]

    return output_string_local


output_string = reverse_character_string("Hello World Morning")
print(output_string)
