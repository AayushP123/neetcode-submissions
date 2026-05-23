class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        subset = []


        def subsets(subset, i):
            ans.append(subset.copy())

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                subset.append(nums[j])
                subsets(subset, j + 1)
                subset.pop()
        subsets(subset, 0)
        return ans