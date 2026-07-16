class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # create freq map to map value to amount
        freq = {}

        # Do the mapping
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        # The math is, as long as the count is above 1, there is always
        # A way to solve, using just 3's and 2's. So create the answer
        # Integer, set it to 0, add however many times its divisible by 3
        # Round up no matter what if the value is above .0, because
        # that means u can also delete two, leading to empty array for answer
        ans = 0
        for count in freq.values():
            if count == 1:
                return -1

            ans += math.ceil(count / 3)
        return ans