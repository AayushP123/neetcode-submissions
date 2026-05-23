class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        pick = [False] * len(nums)
        
        def backtrack(perm):
            if len(perm) == len(nums):
                ans.append(perm.copy())
            
            for i in range(len(nums)):
                if pick[i] == False:
                    perm.append(nums[i])
                    pick[i] = True
                    backtrack(perm)
                    perm.pop()
                    pick[i] = False
        backtrack([])
        return ans