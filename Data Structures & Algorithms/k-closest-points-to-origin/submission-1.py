class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            dist = -(x*x + y*y)
            heapq.heappush(maxHeap, [dist, x, y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        ans = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            ans.append([x, y])
        return ans