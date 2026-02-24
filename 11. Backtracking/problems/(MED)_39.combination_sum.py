class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Important constraint: 2<= candidates[i] <= 40
        res = []

        path = []

        def dfs(index): 
            # Choice
            if sum(path) == target:
                res.append(path.copy())
                return
            elif sum(path) > target:
                return

            # For each candidate
            for i in range(index, len(candidates)): 

                # Decision 1: take this number 
                path.append(candidates[i]) 
                dfs(i)
                path.pop()

        dfs(0)

        return res