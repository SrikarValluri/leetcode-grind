# valid anagram

since the two strings have the same count of letters, I just used a dict to keep track of the letters

I added values to the dict for 1 string, subracted with the other string, the values in the dict should all be 0 else there's smth wrong

use defaultdict to not worry about initializing key and stuff
