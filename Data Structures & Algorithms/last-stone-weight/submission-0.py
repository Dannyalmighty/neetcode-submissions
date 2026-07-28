class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1, stone2 = heapq.heappop(stones), heapq.heappop(stones)
            stone3 = stone1 - stone2
            heapq.heappush(stones, stone3)
        
        stones.append(0)
        return abs(stones[0])