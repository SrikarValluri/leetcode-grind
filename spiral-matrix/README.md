# spiral matrix

I took the opportunity to do some general 2D array practice (traversing across rows and columns, backwards etc.). GPT generated some really important scenarios that I'd like to show here:

For the following matrix, rows and cols:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rows = len(matrix)
cols = len(matrix[0])


To perform a diagonal traversal such all elements on same i + j diagonal (1 | 2 4 | 3 5 7), etc. DO THIS:

for s in range(rows + cols - 1):
    for i in range(rows):
        j = s - i
        if 0 <= j < cols:
            print(matrix[i][j], end=" ")
# Output: 1 2 4 3 5 7 6 8 9


I have NO idea how this works on first or second glance. I need to walk my brain through it multiple times for me to understand it but I don't get it right now.


For the actual spiral problem, I was thinking that my first for loop should iterate through all cells (for x in range(rows*col-1)) and then depending on the x, have 4 different scenarios for each trajectory. However, since going right, down, left, and up can 1) happen so many times, 2) be of different lengths, like you go right 3 down 5 left 2 up 4 right 1 down 3 or whatever it's complicated (also cuz not guarantee square). So I was stuck and saw GPT generated solution:

top, bottom = 0, rows - 1
left, right = 0, cols - 1

while top <= bottom and left <= right:
    for j in range(left, right + 1):  # top row
        print(matrix[top][j], end=" ")
    top += 1

    for i in range(top, bottom + 1):  # right column
        print(matrix[i][right], end=" ")
    right -= 1

    if top <= bottom:
        for j in range(right, left - 1, -1):  # bottom row
            print(matrix[bottom][j], end=" ")
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):  # left column
            print(matrix[i][left], end=" ")
        left += 1
# Output: 1 2 3 6 9 8 7 4 5

So I need to figure out how this works exactly. And then, I'd say I'm prepared to tackle any loops through 2d arrays after understanding these two (the diagonal and the spiral (both inward and outward)).

Will revisit this tomorrow.
