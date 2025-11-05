# first bad version


This was obviously a binary search problem (you have a range of sorted or in sequence values and you're trying to solve for a condition that's given by the API). The tricky part was figuring out the +-s, the small details


the template that I used is

while left < right:
   if condition():
      right = middle
   else:
      left = middle + 1

and with this template, the left will be the MINIMAL value to satisfy the condition. If i want the MAXIMUM value that won't
satisfy the condition, then I return left - 1
