

def is_subsequence(lst, sequence):
    pass




lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))


def is_pangram(my_str):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    my_str = my_str.lower()
    letters_in_str = set(my_str)
    return alphabet.issubset(letters_in_str)



my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))  # True

str2 = "The dog jumped"
print(is_pangram(str2))  