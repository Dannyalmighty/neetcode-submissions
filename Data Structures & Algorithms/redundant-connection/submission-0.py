class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))  # nodes are 1-indexed per problem convention

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x

        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return False  # already connected — this edge is redundant
            parent[root_x] = root_y
            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]

        return []  # shouldn't reach here per problem guarantees