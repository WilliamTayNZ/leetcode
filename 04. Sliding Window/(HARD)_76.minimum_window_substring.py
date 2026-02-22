class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_counter = Counter(t)

        t_chars_remaining = len(t)
        min_window = (0, float("inf")) # A useful way to initialise a default min window
        l = 0

        for r, char in enumerate(s): # index, s[index]
            if t_counter[char] > 0: # Note that missing characters are gracefully handled by Counter which returns 0
                t_chars_remaining -= 1
            t_counter[char] -= 1

            if t_chars_remaining == 0: # l and r bounds a valid substring
                while True:
                    if t_counter[s[l]] == 0: # Will break when the min substring ending at r is found
                        break
                    t_counter[s[l]] += 1 # Handled gracefully by Counter for missing characters
                    l += 1
                
                if r-l < min_window[1] - min_window[0]:
                    min_window = (l, r)
                
                t_counter[s[l]] += 1
                t_chars_remaining += 1
                l += 1
        
        if min_window[1] == float("inf"):
            return ""
        else:
            return s[min_window[0]:min_window[1] + 1]

# November 29th, 2025