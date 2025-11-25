# clone graph


In order to clone the graph, we did 3 steps that are slightly different from template BFS algorithm:

1) the visited set is now a dictionary which keeps track of each VALUE of each node (because the values of the nodes as stated in the problem are indexed in order of the nodes)

2) for each ORIGINAL node that gets added in the queue, check each of its neighbors, add to queue, and also update the visited dict with new Nodes for each value.

3) the clone of the original node's neighbors need to be updated in the loop as well.


Eventually, you can just return visited[start_node.val] which is the clone of the start node which is auto attached to the rest of the cloned graph.


GG
