class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            tempAns = numbers[l] + numbers[r]
            if tempAns < target:
                l += 1
            elif tempAns > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        return []