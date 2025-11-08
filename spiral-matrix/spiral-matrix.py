class Solution:
    def normalTraversal(self, matrix: List[List[int]]) -> List[int]:
        normal = []
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                normal.append(matrix[i][j])

        return normal

    def bottomUpTraversal(self, matrix: List[List[int]]) -> List[int]:
        # bottom to top
        bottom_up = []
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows-1, -1, -1):
            for j in range(cols):
                bottom_up.append(matrix[i][j])

        return bottom_up

    def columnTraversal(self, matrix: List[List[int]]) -> List[int]:
        # display from columns 1, 4, 7, 2, 5, 8, etc.
        columns = []
        rows, cols = len(matrix), len(matrix[0])
        for j in range(cols):
            for i in range(rows):
                columns.append(matrix[i][j])

        return columns

    def backwardsEverythingTraversal(self, matrix: List[List[int]]) -> List[int]:
        backwards_everything = [] # 9 6 3 8 5 2...
        rows, cols = len(matrix), len(matrix[0])
        for j in range(col-1, -1, -1):
            for i in range(row-1, -1, -1):
                backwards_everything.append(matrix[i][j])

        return backwards_everything

    def diagonalTraversal(self, matrix: List[List[int]]) -> List[int]:
        only_diagonal = [] # assuming square
        rows, cols, len(matrix), len(matrix[0])
        if rows == cols:
            for i in range(rows):
                only_diagonal.append(matrix[i][i])
        return only_diagonal

    def zigZagTraversal(self, matrix: List[List[int]]) -> List[int]:
        zigzag = []
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            if i % 2:
                for j in range(cols):
                    zigzag.append(matrix[i][j])
            else:
                for j in range(cols-1, -1, -1):
                    zigzag.append(matrix[i][j])
        return zigzag

    def zigZagColumnTraversal(self, matrix: List[List[int]]) -> List[int]:
        zigzag = []
        rows, cols = len(matrix), len(matrix[0])
        for j in range(cols):
            if j % 2:
                for i in range(rows):
                    zigzag.append(matrix[i][j])
            else:
                for i in range(rows-1, -1, -1):
                    zigzag.append(matrix[i][j])
        return zigzag

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        for x in range(rows * cols - 1):
            pass
            
