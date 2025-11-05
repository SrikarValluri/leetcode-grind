# ransom note


This question was simple to use a dictionary for. I parsed the number of characters that I could use by storing them in a dictionary.
When determining if I had enough characters to generate the string, I just subtracted the letter count from the dictionary. I then checked if I had any negative numbers in the values of the dictionary (ensuring that I had enough letters to generat the string) and returned that condition.
