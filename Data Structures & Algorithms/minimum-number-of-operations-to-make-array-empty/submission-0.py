class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0

        for num, cnt in count.items():
            if cnt == 1:
                return -1
            ans += math.ceil(cnt / 3)
        
        return ans