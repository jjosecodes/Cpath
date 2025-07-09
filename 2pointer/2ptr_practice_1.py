# reverse array inplace
"""
Given an array A, use two pointers (i = 0, j = len(A) - 1)
to swap A[i] and A[j] and move inward until
i >= j. Return the reversed array.
"""


def reverse_array(A):
    i = 0
    j = len(A) - 1

    while i < j:
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1
    return A


# Test
'''   

arr = [1, 2, 3, 4, 5]
print("Input: ", arr)
print("Reversed:", reverse_array(arr))
'''



