class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negatives = [-s for s in stones]

        heapq.heapify(negatives)
        while len(negatives) > 1:
            first = heapq.heappop(negatives)
            second = heapq.heappop(negatives)
            if second > first:
                heapq.heappush(negatives, first - second)

        negatives.append(0)
        return abs(negatives[0])