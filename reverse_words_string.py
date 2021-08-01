# Reverse words in a sentence "Hello World"


def string_reverse_order_words(given_str):
    new_reverse_list = []

    if len(given_str) == 0:
        return

    list_words_str = given_str.split()

    list_words_str.reverse()
    for item in list_words_str:
        new_reverse_list.append(item)

    return new_reverse_list


reverse_list = string_reverse_order_words("Hello World")
print(reverse_list)
