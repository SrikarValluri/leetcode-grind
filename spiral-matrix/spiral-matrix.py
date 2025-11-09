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
        left, right, top, bottom = 0, cols-1, 0, rows-1
        order = []
        while left <= right and top <= bottom:
            for i in range(left, right+1): # go right
                order.append(matrix[top][i])
            top += 1

            for i in range(top, bottom+1): # go down
                order.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left-1, -1):
                    order.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top-1, -1): # go down
                    order.append(matrix[i][left])
                left += 1

        return order
