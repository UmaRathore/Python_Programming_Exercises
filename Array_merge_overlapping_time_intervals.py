# You are given an array (list) of interval pairs as input where each interval has a start and end timestamp.
# The input array is sorted by starting timestamps.
# You are required to merge overlapping intervals and return a new output array.

# Expected output_pairs = [(1, 5), (6, 10), (9, 15)]

# Time complexity = O(N)
# Space complexity = O(N)


def merge_overlap_intervals():

    given_pairs = [(1, 5), (6, 10), (7, 8), (9, 15), (10, 12), (13, 14)]
    output_pairs = [(1, 5)]

    if len(given_pairs) == 0:
        return

    for element in given_pairs:
        if output_pairs.count(element) == 0:
            last_element = output_pairs[len(output_pairs) - 1]
            if last_element[1] > element[0] and last_element[1] >= element[1]:
                continue
            else:
                output_pairs.append(element)
        else:
            continue

    print(output_pairs)


merge_overlap_intervals()

