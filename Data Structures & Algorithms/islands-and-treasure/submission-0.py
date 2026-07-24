class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return

        rows, cols = len(grid), len(grid[0])
        queue = deque()

        # Step 1: seed the queue with all treasure chests
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        # Step 2: BFS outward from all treasures simultaneously
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows and 0 <= nc < cols
                    and grid[nr][nc] == 2147483647  # unvisited land
                ):
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))