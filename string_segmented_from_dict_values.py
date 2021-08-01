# Strings: String segmentation
# You are given a dictionary of words and a large input string.
# You have to find out whether the input string can be completely segmented into the words of a given dictionary.
#  The following example elaborates on the problem further.

# declare global variables

given_dictionary = {
        0: 'apple',
        1: 'pear',
        2: 'orange'
}
given_string = 'applepear'


# define function
def string_seg_from_dict(given_dict, given_str):

    output_list = []
    key = 0

    # check for dict and str len not zero
    if len(given_dict) == 0 and len(given_str) == 0:
        return

    # for each key, value in given_dict:
    while key < len(given_dict):

        if given_str.find(given_dict[key]) != -1:
            if given_dict[key] in output_list:
                key += 1
                continue
            else:
                output_list.append(given_dict[key])
                given_str.strip(given_dict[key])
                key += 1
        else:
            key += 1
            continue

    # to check string is fully segmented or not
    if len(given_str) == 0:
        print("not fully segmented")
    else:
        print("fully segmented")

    return output_list


expected_output_list = string_seg_from_dict(given_dictionary, given_string)
print(expected_output_list)
