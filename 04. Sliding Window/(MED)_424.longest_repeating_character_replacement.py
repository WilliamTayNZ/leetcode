class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest_length = 0
        l = 0
        maxf = 0

        for r in range(l, len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1

            maxf = max(maxf, count[s[r]])

            while r-l+1 - maxf > k:
                count[s[l]] -= 1
                l += 1

            longest_length = max(longest_length, r-l+1)

        return longest_length


# November 12th, 2025
