# Given an integer array, move all elements that are 0 to the left
# while maintaining the order of other elements in the array.
# The array has to be modified in-place.
# Try it yourself before reviewing the solution and explanation.


import array as arr
user_array = arr.array("i", [1, 7, 0, 9, 5, 8, 0, 4])


def func_move_zeros():
    zero_count = 0
    given_array = user_array
    for element in given_array:
        if element == 0:
            zero_count += 1
            given_array.remove(0)
    func_insert_zero(given_array, zero_count)
    print(given_array)


def func_insert_zero(given_array, zero_count):
    count = 0
    while count < zero_count:
        given_array.insert(0, 0)
        count += 1


func_move_zeros()
