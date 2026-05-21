class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                ans.append(subset.copy())
                return
            
            # Include number:
            subset.append(nums[i])
            dfs(i + 1)

            # Don't include number:
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return ans