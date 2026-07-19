class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Create pointer that basically writes whether or not to put
        # Current pointer value in the list, else continue
        # This therefore results in a list without unnecessary values
        # PROPERLY SIZED
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k