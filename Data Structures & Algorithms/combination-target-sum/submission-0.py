class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        subset = []

        def dfs(i, cur, total):
            if total == target:
                ans.append(subset.copy())
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                subset.append(nums[j])
                dfs(j, cur, total + nums[j])
                subset.pop()
        dfs(0,[],0)
        return ans