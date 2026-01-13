# Given an integer x, return true if x is a

# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        rev=0
        while temp>0:
            r=temp%10
            temp//=10
            rev=rev*10+r

        if rev==x:
            return True
        else:
            return False