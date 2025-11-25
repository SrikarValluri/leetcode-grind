# validate binary search tree

In order to validate the binary search tree, as we traverse down each side of the tree, we can provide a modified range at which the value should be in. For example, every tree to the left of the root node needs for the maximum value to be (root.val-1). The range can continue to be modified until the root hits None, in which it can return True. It will return false if it's not within bounds. Pretty nice recursive example with a smart solution.
