# number of islands

Essentially, I recognized that whenever we hit a "piece" of land, we propogate (perform a DFS). We can mark all of the nodes we visit within this propogation. Once we hit a dead end, we resolve. Now, we have all of one island marked, and I can increment a counter by 1. Then we do this again whenever we see another piece of land. In this way, we hit all the islands and also make sure to have proper base cases (make sure we return when i, j is out of bounds and if the node is already visited).
