# binary tree level order traversal

This problem is essentially a slight extension for the BFS algorithm. The BFS algorithm uses a set that keeps track of all the nodes visited, as well as a queue that keeps track of the next node to visit.
Whenever we visit a node, we check for the left and right nodes (ensuring they are not null) and add them to the queue. In this way, each level is traversed in-order.

What makes this problem slightly more complicated than a normal BFS is the fact that we have to keep track of each level, and output each value in its own list per level. To track this,
I decided to use a defaultdict with the key being the level, and the values being appened to the default lists. In this way, when we retrieve the dict.values(), it automatically formats the output
just like how the function wants it, per level, and it's already in order because of the BFS.


It was a satisfying problem to solve for sure. The important thing here is to memorize the BFS template (here's a GPT version):

def bfs(graph, start_node):
    """
    Performs a Breadth-First Search on a graph.

    Args:
        graph (dict): An adjacency list representing the graph,
                      where keys are nodes and values are lists of their neighbors.
        start_node: The starting node for the BFS traversal.

    Returns:
        list: A list of nodes in the order they were visited.
    """
    visited = set()  # To keep track of visited nodes
    queue = deque([start_node])  # Initialize queue with the start node
    visited.add(start_node)
    traversal_order = []

    while queue:
        current_node = queue.popleft()  # Dequeue a node
        traversal_order.append(current_node)

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)  # Enqueue unvisited neighbors
    return traversal_order


I knew I had to use BFS here so I learned this format, and now I can solve any problem of this type by first starting with the BFS template and adding onto it.
