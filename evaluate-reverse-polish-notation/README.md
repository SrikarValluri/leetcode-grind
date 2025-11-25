# evaluate reverse polish notation

The wikipedia page linked in the leetcode problem mentioned that a stack implementation should be used to evaluate the notation. It's quite simple: If we go from left to right, we can very simply append each number to the stack. If there are any operations, we remove the previous two numbers in the stack, perform the operation, and then add the result to the stack (this takes care of order of operations etc.) For division it's required to round to whatever is closer to 0 (so I used int() for this).

Relatively straightforward.
