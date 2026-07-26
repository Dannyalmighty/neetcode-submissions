class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n - 1):
            return False
        
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visit = set([0])
        queue = deque([0])

        while queue:
            node = queue.popleft()
            for ne in graph[node]:
                if ne not in visit:
                    visit.add(ne)
                    queue.append(ne)
        
        return len(visit) == n