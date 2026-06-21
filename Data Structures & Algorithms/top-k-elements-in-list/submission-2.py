class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}

        for n in nums:
            mapping[n] = mapping.get(n, 0) + 1
        
        sorted_vals = sorted(mapping.items(), key=lambda item: (item[1], item[0]), reverse=True)

        all_vals = []
        for x in range(k):
            pair = sorted_vals[x]
            key = pair[0]
            all_vals.append(key)
        return all_vals