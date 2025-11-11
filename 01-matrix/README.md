# 01 matrix


Here was my original implementation:

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        memo = {}
        def distance(i, j):
            if i > (m-1) or i < 0 or j > (n-1) or j < 0:
                return float("inf")

            if (i, j) in memo:
                return memo[(i, j)]

            if mat[i][j] == 0:
                memo[(i, j)] = 0
                return memo[(i, j)]


            memo[(i, j)] = 1+min(distance(i+1, j), distance(i-1, j), distance(i, j+1), distance(i, j-1))
            return memo[(i, j)]

        res = []
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(distance(i, j))

            res.append(temp)

        return res


I chose a DFS + memo approach to solve this problem. However, I kept running into an infinite recursion situation, leaving me confused.
I MEMOIZE every output, so how in the world won't (if something is resolved) just get the value from the memo. I put this into GPT, and GPT told me the key learning:
----------
Key idea

Memo only protects you AFTER a cell’s distance is fully computed.
Until that moment, DFS can bounce back and forth between neighbors forever.

You are assuming:
“If I visit something again, memo will stop it.”
That is only true after you have finished computing the value for that cell.

The real problem:

When DFS is still inside the call stack for a cell, that cell is not in memo yet.

This means if DFS tries to revisit it during its own computation, you loop.

Example where your original code fails

Take a simple 2×2 matrix of all 1s:

1 1
1 1


Walk through your original code for (0,0):

For (0,0):

It tries:

distance(1,0)

distance(-1,0)

distance(0,1)

distance(0,-1)

Let’s follow distance(0,1):

For (0,1):

It tries:

distance(1,1)

distance(-1,1)

distance(0,2)

distance(0,0)

Wait.
distance(0,1) calls distance(0,0) again.
---------

So basically my approach doesn't work very well. I should use BFS which is much easier (GPT/Solutions recommend).
