# linked list cycle

Simple soln- keep track of each visited node. If I revisit a node, there's a cycle.

I also saw this implementation of a Floyd's Cycle-Finding algorithm. If a slow pointer and a fast pointer that goes twice the speed are released at the same time, eventually the pointers should catch up to each other if there's a cycle.
