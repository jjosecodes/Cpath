'''

Given a string s consisting of lowercase and/or uppercase 
English letters and digits, return all possible strings 
that can be formed by changing the case of the 
letters in s. You may not alter the order of 
characters in the string, and digits should remain 
unchanged.

'''

# u - digits cant be changed 
# letters have lower and upper cases 

# solve using recursion take base and then go through other possible combinations




def Cases(s:str):
    result = []

    def backtrack(index , pth):
        if index == len(s):
            result.append(pth)
            return
        if s[index].isdigit():
            backtrack(index + 1 , pth + s[index])
        else:
            backtrack(index + 1 , pth + s[index].lower())
            backtrack(index + 1 , pth + s[index].upper())
    backtrack(0, "")
    return result

print(Cases("a1b2"))



# explain more while coding 






# khogali ibrahim
















