class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        res = 0

        def bfs(r, c):
            queue = deque([(r, c)])
            while queue:
                row, col = queue.popleft()
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        queue.append((nr, nc))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    res += 1
                    bfs(r,c)
        
        return res