class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {')':'(', '}':'{',']':'['}

        for char in s:
            if char not in mapping:
                stack.append(char)
            elif not stack:
                return False
            else:
                top = stack.pop() # By default, no index means last element of array is popped
                if mapping[char] != top:
                    return False
        
        if stack:
            return False
        return True

# November 29th, 2025