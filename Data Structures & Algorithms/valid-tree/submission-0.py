class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
            
        preMap = {n: [] for n in range(n)}
        for a, b in edges:
            preMap[a].append(b)
            preMap[b].append(a)

        visit = set([0])
        queue = deque([0])
        while queue:
            node = queue.popleft()
            for ne in preMap[node]:
                if ne not in visit:
                    queue.append(ne)
                    visit.add(ne)
        return len(visit) == n
