class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]  # negate to simulate a max-heap
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)   # largest
            second = -heapq.heappop(max_heap)  # second largest

            if first != second:
                heapq.heappush(max_heap, -(first - second))
            # if equal, both are destroyed — push nothing

        return -max_heap[0] if max_heap else 0