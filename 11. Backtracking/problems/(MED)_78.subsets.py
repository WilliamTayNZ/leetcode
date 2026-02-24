class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Base case
        # Choices
        # Constraints
        # Backtracking step

        result = []
        path = []

        def dfs(index):
            # For loop is for exploration

            # If we've traversed all numbers, stop
            if index == len(nums):
                result.append(path[:])
                return

            # Decision: include nums[i]
            path.append(nums[index])
            dfs(index+1)

            # Decision: don't include nums[i]
            path.pop()
            dfs(index+1)

            # Choose a number to add to the path, then continue searching the rest of the space
            # Undo this choice, then choose another number to add


        dfs(0)

        return result
    
# TRY AGAIN LATER