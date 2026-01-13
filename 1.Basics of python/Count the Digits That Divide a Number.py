# Given an integer num, return the number of digits in num that divide num.

# An integer val divides nums if nums % val == 0.

 

# Example 1:

# Input: num = 7
# Output: 1
# Explanation: 7 divides itself, hence the answer is 1.



class Solution:
    def countDigits(self, num: int) -> int:
        temp=num
        c=0
        while temp>0:
            r=temp%10
            if num%r==0:
               c=c+1
            temp//=10
        return c
