class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Given a set of numbers in increasing order
        # Indexs' are 1-indexed
        # Return value of each index, must equal the target val
        # index1 < index2

        l = 0
        r = len(numbers) - 1
        
        while l < r:
            tempAns = numbers[l] + numbers[r]

            if tempAns > target:
                r -= 1
            elif tempAns < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []