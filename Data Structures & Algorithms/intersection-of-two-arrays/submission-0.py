class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numsUne = set(nums1)
        numsDeux = set(nums2)
        ans = []

        for num in numsUne:
            if num in numsDeux:
                ans.append(num)
        return ans