class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prev_height):
            if (
                (r, c) in visited
                or r < 0 or r >= rows
                or c < 0 or c >= cols
                or heights[r][c] < prev_height
            ):
                return
            visited.add((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # Start from Pacific borders: top row and left column
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])

        # Start from Atlantic borders: bottom row and right column
        for c in range(cols):
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        return list(pacific & atlantic)