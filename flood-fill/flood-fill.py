class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])

        old_color = image[sr][sc]
        if old_color != color:
            image[sr][sc] = color

            if (sr+1) >= 0 and (sr+1) <= rows-1 and image[sr+1][sc] == old_color:
                image = self.floodFill(image, sr+1, sc, color)

            if (sr-1) >= 0 and (sr-1) <= rows-1 and image[sr-1][sc] == old_color:
                image = self.floodFill(image, sr-1, sc, color)

            if (sc+1) >= 0 and (sc+1) <= cols-1 and image[sr][sc+1] == old_color:
                image = self.floodFill(image, sr, sc+1, color)

            if (sc-1) >= 0 and (sc-1) <= cols-1 and image[sr][sc-1] == old_color:
                image = self.floodFill(image, sr, sc-1, color)

        return image
