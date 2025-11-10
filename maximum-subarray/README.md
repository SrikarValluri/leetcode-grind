# maximum subarray

What is important to realize here is that two counts are required (this is technically a dp problem). We need a variable for the the sum of the current sequence, and also the max sum of any sequence. If our current sum is negative, we know that it's not the most optimal, and we just reset it to 0, essentially reseting the sequence. We keep track of the max sequence that we've had at any point, and that's what we return. If the max sequence is 0, it means that there are only negative numbers within the array, so we just retrieve the maximum value from the entire array. 
