# add binary


I did this stuff in assembly language, where you had to keep track of the carry bit. Essentially, I looped backwards for each binary string, added each individual digit (with the carry bit) and then determined if we needed to carry for the following digit. Eventually, since we know that a and b are potentially two different lengths, we have to determine whether one of them hits the beginning before the other one, and if so, we just set that value to 0 (which is what I had in the condition in the beginning of the loop). In the end, we make sure to add the carry bit remaining. 
