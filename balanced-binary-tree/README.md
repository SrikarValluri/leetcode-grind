# balanced binary tree


Need to calculate height of each subtree, so I created a helper function to do this.
Then, recursing through each node, checking whether the left and right subtrees are balanced, and also if the height delta between the left and right subtrees is <= 1


I found a more efficient solution, where instead of recursing seperately for the height, you directly incorporate checking the height delta for a subtree and only returning the height if the height delta is within bounds. 
