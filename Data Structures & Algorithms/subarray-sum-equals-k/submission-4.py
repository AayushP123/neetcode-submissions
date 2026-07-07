class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Create result variable, holding possible ways,
        # Create curSum, which is current subarray sum
        # Create hashmap mapping of prefixSum, and count for it
        # Do curSum - k value, check if that count is in PrefixSum
        # If so, add count to result, remove 1 count value from hashmap
        prefixSum = {0 : 1}
        res = 0
        curSum = 0

        for n in nums:
            curSum += n
            val = curSum - k
            if val in prefixSum:
                res += prefixSum[val]
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)
        return res