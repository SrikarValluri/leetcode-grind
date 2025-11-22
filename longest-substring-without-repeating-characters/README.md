# longest substring without repeating characters

Basically, we iterate through each character in the string with a right pointer. Whenever we hit charater that we've already seen before, we iterate the left pointer until the string s[left:right+1] does not include any repeating characters. The best way to keep track of that is by using a set that keeps track of the "visited" characters. Whenever we see, while iterating through the string, that the left pointer has hit smth that's in the set, then we keep iterating the left pointer, removing what the left pointer is seeing form the set until we no longer see the whatever the right pointer's pointing too.
We keep track of the longest value (distance between left and right pointer), and update it whenever we have a bigger value.
