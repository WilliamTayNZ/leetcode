from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Return true if t and s use the exact same pieces to build their word

        hashmap = {}

        # Key = character, Value = count

        for i in range(len(s)):
            character = s[i]
            if character not in hashmap:
                hashmap[character] = 1 # The count
            else:
                hashmap[character] += 1

        if len(t) != len(s):
            return False

        else:
            for chr in t:
                if chr in hashmap and hashmap[chr] > 0:
                    hashmap[chr] -= 1
                else:
                    return False

            return True
                

solution = Solution()

print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram("rat", "car"))
print(solution.isAnagram("abc", "ab"))