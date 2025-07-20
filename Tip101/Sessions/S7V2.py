




def is_nested(paren_s):
    if not paren_s:
        return True
	
    if paren_s[0] == '(' and paren_s[-1] == ')':
        return is_nested(paren_s[1:-1])

    return False 


#print(is_nested("(()))"))

def count_ones(lst):
    if not lst:
        return -1
    
    left = 0
    right = len(lst) - 1
    middle = -1

    while left <= right:
        mid = (left + right) // 2 
        if lst[mid] == 1 :
            middle = mid  # ex 3 
            right = mid - 1
            # return count_ones(left , mid - 1)
        else:
            left = mid + 1
            # return count_ones(mid + 1 , right )
    return len(lst) - middle    # 10 - 3   

#print(count_ones( [0, 0, 0, 1, 1, 1, 1]))

def binary_search(nums, target, left = 0, right = None):
    if not nums:
        return -1
    
    if right is None:
        right = len(nums) -1 

    if left > right :
        return -1
    
    mid = (left + right ) // 2 


    if nums[mid] == target:
        return mid 
    elif target < nums[mid]:
        return binary_search(nums, target, left, mid - 1)
    else:
        return  binary_search(nums, target, mid + 1, right)

#nums = [1, 3, 5, 7, 9, 11, 13, 15]


#print(binary_search(nums, 13))


def count_rotations(nums):
    left = 0 
    right = len(nums) -1


    while left <= right:
        mid = (left + right) //2
        next_index = (mid +1 ) % len(nums)
        prev_index = (mid -1 + len(nums)) %len(nums ) 
        
        if nums[mid] <= nums[prev_index] and nums[mid] <=nums[next_index]:
            return mid
        elif nums[mid] >= nums[right]:
            left = mid + 1
        else:
            right = mid -1 
    return -1 

print(count_rotations( [8, 9, 10, 2, 5, 6]))

# works now 

