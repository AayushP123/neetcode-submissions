class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create Hashmap, map Value to Index, 

        mapping = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in mapping:
                return[mapping[diff], i]
            mapping[n] = i