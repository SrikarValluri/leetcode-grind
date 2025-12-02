# generate parenthesis

This is a backtracking problem, and it's clear to use this method because the parenthesis generation can happen via a tree. The possibilites can be found via either taking a step, or not taking a step.

What's specifically important about this problem are the constraints and how to deal with them. The two main constraints in this problem are 1) the number of left parentheses should be less than the total number input, and 2) the right parenthesis need to be less in number to the left (otherwise there will be no more left parens to match, resulting in an invalid matching).

The backtracking function takes in left paren count and right paren count, and checks for the two conditions above. If it satsfies either condition, there a left paren will be added to the temporary list, backtrack() will be called again with +1 left or +1 right paren, and then the left paren will be popped for the next potential possibility. In this way it checks all cases.
