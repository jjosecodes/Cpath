

def repeat_hello(n):
	if n > 0:
		print("Hello")
		repeat_hello(n - 1)
		
# repeat_hello(5)

# print(" ----- ")

def repeat_hello_iterative(n):
	for i in range(n):
		print("Hello")
# repeat_hello_iterative(5)


def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)
	

# print(factorial(5))

def sum_list(lst):
	if not lst:
		return 0 
	else :
		return lst[0] + sum_list(lst[1:])
	

# print(sum_list([1, 2, 3, 4, 5]))

# What is the time complexity of this function?
#   O(n)
# What is the space complexity?
# think O(n)


def is_power_of_two(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 != 0 :  # is the remainder of n % 2 NOT 0
        return False
    return is_power_of_two( n // 2)

	#       64 -> 32 -> 16 -> 8 -> 4 -> 2
	#       65 ->  3
# print(is_power_of_two(64))
# print(is_power_of_two(65))


# def binary_search(lst, target):
	# Initialize a left pointer to the 0th index in the list
	# Initialize a right pointer to the last index in the list
	
	# While left pointer is less than right pointer:
		# Find the middle index of the array
		
		# If the value at the middle index is the target value:
			# Return the middle index
		# Else if the value at the middle index is less than our target value:
			# Update pointer(s) to only search right half of the list in next loop iteration
		# Else
			# Update pointer(s) to only search left half of the list in next loop iteration
	
	# If we search whole list and haven't found target value, return -1

def binary_search(lst, target):
    left = 0
    right = len(lst) -1
	
    while left <= right:
        mid = (left + right) // 2
		
        if lst[mid] ==target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# lst = [1, 3, 5, 7, 9, 11, 13, 15]
# target = 11
# print(binary_search(lst, target))


def find_last(lst, target):
    left = 0
    right = len(lst) -1
    result = -1

    while left <= right:
        mid = (left + right) // 2
		
        if lst[mid] ==target:
            result = mid
            left = mid +1 
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

#lst = [1, 3, 5, 7, 9, 11, 11, 13, 15]
#target = 11

#print(find_last(lst, target))

def find_floor(lst, x):
    left = 0
    right = len(lst) -1
    result = -1

    while left <= right:
        mid = (left + right) // 2
		
        if lst[mid] ==x:

            return mid
        elif lst[mid] < x:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result