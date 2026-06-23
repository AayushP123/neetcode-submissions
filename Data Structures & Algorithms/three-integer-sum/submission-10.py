class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i, n in enumerate(nums):
            if n > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = nums[l] + nums[r] + n

                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    ans.append([nums[l], n, nums[r]])
                    l += 1
                    r -= 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
        return ans