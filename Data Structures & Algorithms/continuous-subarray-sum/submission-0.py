class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Store remainder -> end index in prefixSum
        prefix = {0 : -1}
        total = 0

        for i, num in enumerate(nums):
            total += num
            r = total % k
            if r not in prefix:
                prefix[r] = i
            elif i - prefix[r] > 1:
                return True
        return False