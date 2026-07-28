class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = Counter(tasks)
        max_heap = [-f for f in freqs.values()]
        heapq.heapify(max_heap)

        time = 0
        cooldown_queue = deque()  # stores (available_time, remaining_count)

        while max_heap or cooldown_queue:
            time += 1

            if max_heap:
                count = 1 + heapq.heappop(max_heap)  # do one unit of the most frequent task
                if count < 0:
                    cooldown_queue.append((time + n, count))

            if cooldown_queue and cooldown_queue[0][0] == time:
                _, count = cooldown_queue.popleft()
                heapq.heappush(max_heap, count)

        return time