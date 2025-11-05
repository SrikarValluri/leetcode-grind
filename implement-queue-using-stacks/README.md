# implement queue using stacks

Very straightforward. In order to implement a FIFO queue, either the peeking/popping has to be inefficient, or the insert has to be inefficient.

I chose the inserting to be inefficient. Whenever a number is added to the queue, it is added to the beginning of the list.
Whenever a value needs to be peeked or popped, it happens at the end of the queue.
