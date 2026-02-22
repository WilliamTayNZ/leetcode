from typing import List

# Easier on the eyes
class NewCleanerSolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = []

        hashmap = {} # sorted_string -> original_string

        for string in strs: # O(n)
            sorted_string = ''.join(sorted(string)) # O(klogk)

            if sorted_string in hashmap:
                hashmap[sorted_string].append(string)
            else:
                hashmap[sorted_string] = [string]

        for sorted_string in hashmap:
            anagram_groups.append(hashmap[sorted_string])
        
        return anagram_groups

# Slightly less constant space overhead because dicts store indices and not lists
class OldSolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        first_string = strs[0]
        anagram_groups = [[first_string]] # Initialises with 1 group containing the first string in the array

        # Hashmap to map the sorted string (identifier) to the index of associated group in anagram_groups
        anagram_to_group_dict = {}
        anagram_to_group_dict[''.join(sorted(first_string))] = 0

        for i in range(1,len(strs)): # For each remaining string in array
            string = strs[i]
            sorted_string = ''.join(sorted(string))

            if sorted_string in anagram_to_group_dict:
                group_index = anagram_to_group_dict[sorted_string]
                anagram_groups[group_index].append(string)

            else: # Create new group
                anagram_to_group_dict[sorted_string] = len(anagram_groups)
                anagram_groups.append([string])

        return anagram_groups


solution = NewCleanerSolution()

print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(solution.groupAnagrams([[""]]))
print(solution.groupAnagrams([["a"]]))
print(solution.groupAnagrams([
    "eat", "tea", "tan", "ate", "nat", "bat",
    "tab", "bat", "tap", "pat", "apt",
    "rat", "tar", "art", "star", "tars", "cheaters", "teachers", "hectares"
]))
