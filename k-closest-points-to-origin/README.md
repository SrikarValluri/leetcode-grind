# k closest points to origin

The solution to this problem was quite simple. Calculate the distance (I didn't bother with the square root because sqrt(a) will always be greater than sqrt(b) if a > b). Keep in some sort of dictionary, and sort from lowest to highest distance, and return the first k points. Very simple question.
