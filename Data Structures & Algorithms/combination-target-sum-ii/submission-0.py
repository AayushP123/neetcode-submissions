class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        subsets = []

        def dfs(i, cur, total):
            if total == target:
                ans.append(subsets.copy())
            
            for j in range(i, len(candidates)):
                if total + candidates[j] > target:
                    break
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                subsets.append(candidates[j])
                dfs(j + 1, cur, total + candidates[j])
                subsets.pop()
        dfs(0, [], 0)
        return ans