# max profit

1) use 2 pointers
2) start iterating the right pointer
3) if the price on the right is greater than the price on the left, then we calculate all the potential max profits > 0
4) if p_right < p_left, that means we've calculated all the maximum profits we can until then, we've already saved the max, so now p_right becomes our new p_left and we keep going
