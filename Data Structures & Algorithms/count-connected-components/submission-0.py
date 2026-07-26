class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visit = set()
        count = 0

        def dfs(node):
            visit.add(node)
            for ne in graph[node]:
                if ne not in visit:
                    dfs(ne)
        
        for node in range(n):
            if node not in visit:
                count += 1
                dfs(node)
        
        return count