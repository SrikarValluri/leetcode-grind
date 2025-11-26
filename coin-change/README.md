# coin change


The question is asking to return the MINIMUM number of coins required for the amount provided. This is like the template of a DP problem. We can break this problem down into subproblems for the minimum number of coins required for each amount from 0 -> amount. While iterating through amount, we can check whether that particular amount is greater than the value of the coin, and if so, then we can update the dp that holds the minimum number of coins required by setting it to the min(itself, 1+dp[current_amt-coin]). This guarantees that we get the best possible count of the minimum number of coins from all potential possibilites being explored and updated.
