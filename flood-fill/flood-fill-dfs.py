class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        old_color = image[sr][sc]
        visited = set()

        def dfs(r, c):
            if r < 0 or r > rows-1 or c < 0 or c > cols-1 or ((r, c) in visited) or image[r][c] != old_color:
                return

            image[r][c] = color
            visited.add((r, c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        dfs(sr, sc)
        return image
