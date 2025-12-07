# next permutation

The algorithm is as follows: 1) identify the digit (from the back to the front) in which you need to swap by ensuring that it's larger that the value after it. This is the starting point. Then, 2) swap every digit from the end to the digit that we detected prior IF the digit prior is greater than the current digit. Finally, 3) reverse every digit from the end to the digit identified prior. By doing this, we get the next permutation within the sequence. 
