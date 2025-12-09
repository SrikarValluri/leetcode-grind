# string to integer (atoi)

This problem required a lot of parsing and has a lot of logic associated with it, which unfortunately made the code a bit messy. Essentially, I have to do a check to remove whitespace or trailing 0s. Then, I need to check for a positive or negative sign. Then I check for trailing 0s again. Then I look for the actual value. Then I have to stop processing the string if there are random characters after the value. Then I convert that string into an integer successfully and return that to the user. Some edge cases that I had to deal with were dealing with empty strings at multiple points during the implementation.


UPDATE: redid the logic to 1) turn string into list first to increase space complexity and 2) simplified logic so that I'm not checking the same thing multiple times. Much cleaner and simpler solution.
