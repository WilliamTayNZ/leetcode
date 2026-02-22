from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_counter = Counter(s1)

        l = 0
                
        for r in range(0, len(s2)):
            # The character satisfies conditions to be part of a possible permutation
            if s2[r] in s1_counter and s1_counter[s2[r]] > 0: 
                s1_counter[s2[r]] -= 1

                if s1_counter[s2[r]] == 0 and r-l+1 == len(s1):
                    return True

            # We found character not in s1, so we have to reset counter and start ahead of the character
            elif s2[r] not in s1_counter: 
                while l < r:
                    s1_counter[s2[l]] += 1
                    l += 1
                l += 1 # to skip character not in s1

            # The character is in s1, but there are too many in our window now            
            elif s1_counter[s2[r]] == 0:
                s1_counter[s2[r]] -= 1
                while s1_counter[s2[r]] < 0:
                    s1_counter[s2[l]] += 1
                    l += 1

        return False

# November 16th, 2025
