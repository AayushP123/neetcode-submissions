class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a hash map, mapping value to index
        # enumerate list, obtain index and corresponding value for each list index
        # Target - current list value, Obtain the potential answer
        # Check if the answer is in the hashmap we created, return hashmap value, current index
        # Add value to hashmap

        mp = {}
        for i, n in enumerate(nums):
            ans = target - n
            if ans in mp:
                return [mp[ans], i]
            mp[n] = i