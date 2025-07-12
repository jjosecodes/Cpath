


def count_mississippi(limit):
    for num in range(1, limit):
        print( f"{num} mississippi")

#count_mississippi(6)
                


def swap_ends(my_str):
    if len(my_str) < 2:
        return my_str
    return my_str[-1] + my_str[1:-1] + my_str[0]
'''
my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)
'''


def is_pangram(my_str):
    new_str = my_str.lower()
    word = set(ch for ch in new_str if 'a' <= ch <= 'z')
    return len(word) == 26

my_str = "The quick brown fox jumps over the lazy dog"
#print(is_pangram(my_str))

str2 = "The dog jumped"
#print(is_pangram(str2))





def reverse_string(my_str):
    return my_str[::-1]

#my_str = "live"
#print(reverse_string(my_str))



def first_unique_char(my_str):
    for i, ch in enumerate(my_str):
        if my_str.count(ch) == 1:
            return i
    return -1

''' 
my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))
'''


def min_distance(words, word1, word2):
    min_dist = float('inf')
    index1 = index2 = -1
    
    for i, word in enumerate(words):
        if word == word1:
            index1 = i
        if word == word2:
            index2 = i

        if index1 != -1 and index2 != -1:
            min_dist = min(min_dist, abs(index1 - index2))
    return min_dist if min_dist != float('inf') else -1




words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)



