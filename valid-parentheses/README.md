# valid parentheses

1) iterate through the string
2) whenever you see left paren, bracket, etc. add it to stack
3) whenever you see right paren, ensure a)stack isn't empty, b) popped value from stack is counterpart of current char
4) if fails that check, then it's not a match
5) also check at end to make sure stack is empty, otherwise there's smth missing
