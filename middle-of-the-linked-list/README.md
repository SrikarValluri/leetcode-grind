# middle of the linked list

Very straightforward here- first I need to go through the entire linked list to determine the number of nodes. I know the middle node according to the definition given in the problem (if odd #, then the middle, if even #, then the second middle) is num_nodes // 2 + 1, so from the head, I would loop num_nodes // 2 times to get the node that's in the middle.
