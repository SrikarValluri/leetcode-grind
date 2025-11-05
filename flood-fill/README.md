# flood fill

I decided recursion made the most intuitive sense, because the color proliferates to its adjacent values easier

1) find the starting position, check if it's the same as old color, if it isn't, then change it
2) perform the change to left, top, right, down, while checking to make sure it's a valid position in the array
3) treat the recursion as black box assuming it will return properly and then at the end return the full 2d array


UPDATE:
updated solution with specific dfs call. What I was doing before was also dfs, but this made my code cleaner, I didn't have to check for 1 base case 4 times, but should've just done it like this in the first place.
