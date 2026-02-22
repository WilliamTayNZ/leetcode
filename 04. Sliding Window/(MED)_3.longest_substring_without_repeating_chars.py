from collections import defaultdict

class SolutionWithDefaultDict:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter: dict[str, int] = defaultdict(int)

        longest = 0
        l = 0

        for r in range(len(s)):
            counter[s[r]] += 1

            while counter[s[r]] > 1:
                counter[s[l]] -= 1
                l += 1
            
            longest = max(longest, r-l+1)
            

        return longest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0

        if len(s) == 0:
            return 0
        
        longest_length = 1 
        substring_chars = {s[left]: left} # O(n) space complexity

        for right in range(1, len(s)):
            if s[right] in substring_chars: 
                duplicate_index = substring_chars[s[right]] # duplicate index
                longest_length = max(longest_length, right-left)

                while left < duplicate_index + 1:
                    del substring_chars[s[left]]
                    left += 1

                substring_chars[s[right]] = right
            else:
                substring_chars[s[right]] = right
                longest_length = max(longest_length, right+1-left)

        return longest_length