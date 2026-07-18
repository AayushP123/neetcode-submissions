class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        # Set each negative value to 0, we only care about positive val
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        # Check for each value in nums if there is a value less than it
        # That is greater than 0, and a value greater than it.
        # If not, set 0th index to that val
        # Return 0th index of hash
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)
        
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        
        return len(nums) + 1