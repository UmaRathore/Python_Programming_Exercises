def isBalanced(s):
    # Write your code here

    seq = {
        '{': '}',
        '(': ')',
        '[': ']'
    }

    itr = 0
    lseq = []
    output = True
    count = 0
    desired = ""
    if len(s) == 0:
        return output

    if len(s) % 2 != 0:
        output = False
        return output

    while itr < len(s):

        val = s[itr]
        for key, value in seq.items():

            if val != value:
                count += 1
            else:
                desired = key
                count = 0
                break

        if count > 0:
            lseq.append(s[itr])
            count = 0

        if lseq[len(lseq)-1] == desired:
            lseq.pop(len(lseq)-1)
            output = True
        else:
            output = False

        itr += 1

    return output


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
    print('[\"', string, '\"]', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    s1 = "{[(])}"
    expected_1 = False
    output_1 = isBalanced(s1)
    check(expected_1, output_1)

    s2 = "{{[[(())]]}}"
    expected_2 = True
    output_2 = isBalanced(s2)
    check(expected_2, output_2)
