# Get size of array from user and its values as integers, return indices of the two numbers such
# that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def sum_integers_as_target_array(nums, target):

    for i in range(len(nums)):
        if nums[i] != target and i != (len(nums)-1):
            j = i+1
            while j < len(nums):
                sum_num = nums[j] + nums[i]
                if sum_num == target:
                    print(f'index of {nums[i]} is: {nums.index(nums[i])}')
                    print(f'index of {nums[j]} is: {nums.index(nums[j])}')
                    print(f'sum of {nums[i]} and {nums[j]} is {sum_num}')
                j += 1


def data():

    num_array = []
    while True:
        try:
            array_size = int(input('Enter number of items in an Array: '))
        except ValueError:
            print('Value error enter integer')
            continue
        else:
            break
    print(f'Time to enter {array_size} elements in an array')

    for val in range(0, array_size):
        while True:
            try:
                item = int(input())
            except ValueError:
                print('Value error enter integer')
                continue
            else:
                break
        num_array.append(item)
    target_number = int(input('Enter target element: '))
    return num_array, target_number


try:
    num, tar = data()
    sum_integers_as_target_array(num, tar)
except TypeError:
    print('Type error - include a return statement')
