from typing import List

from collections import Counter

class BucketSortSolution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = Counter(nums) # Creates key-value pairs num: frequency
        buckets = [0] * (n + 1) # Creates [0, 0, 0 ...] where index is frequency

        for num, freq in counter.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)

        # Eg. buckets = [ 0, [3], [2], [1], 0, 0, 0 ]

        result = []

        for i in range(n, -1, -1):
            if buckets[i] != 0:
                result.extend(buckets[i])
            if len(result) == k: 
                # We can do this since it is guaranteed answer is unique
                # Otherwise, multiple numbers could tie for frequency at the cutoff point, so we would need check len(result) >= k
                return result

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums) # O(n)

        frequency_to_elements_dict = {}

        for key, value in counter.items(): # O(n)
            if value in frequency_to_elements_dict:
                frequency_to_elements_dict[value].append(key)
            else:
                frequency_to_elements_dict[value] = [key]

        # print(frequency_to_elements_dict.keys())

        frequency_list = list(frequency_to_elements_dict.keys()) # O(f), f <= n)
        frequency_list.sort() # O(flogf), f <= n
        frequency_list.reverse() # O(f)
        # print(frequency_list)

        keys_most_to_least_frequent = []

        for i in range(len(frequency_list)): # O(n) in total
            frequency = frequency_list[i]
            elements = frequency_to_elements_dict[frequency]
            for j in range(len(elements)):
                keys_most_to_least_frequent.append(elements[j])
                if len(keys_most_to_least_frequent) == k:
                    return keys_most_to_least_frequent
        
        # O(n + flogf) time, worst case O(nlogn) time

            
solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3], 2))
print(solution.topKFrequent([1], 1))
print(solution.topKFrequent([1,1,1,2,2,2,2,3,3,4,5,5,5,5,5], 3))
