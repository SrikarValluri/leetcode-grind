# course schedule


The big idea is that we can generate a directed graph with the information given in the problem. For each course, we can generate connections to each prereq that it requires. Then, by determining whether there are any cycles (or dependencies that we cannot resolve) in the graph, then we know that you can't actually complete all the courses.

The DFS algorithm 1) checks if the course even has any prereqs (if it doesn't, it already satisfies the condition returning True) and 2) checks if the course has already been traversed too (in which it returns False). Those were the base cases. Then it checks by iterating through each of the neighbors for each edge (or course) to see whether they have any prereqs or cycles, etc. and if so, return False. If we determine there are no cycles for a course, we say "OK, we are able to reach this" and set all of it's prereqs to 0.

We then call this DFS for each course and see if we ever get False anywhere, and if we do, then there's a cycle.
