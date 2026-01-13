# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

 

# Example 1:

# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp=n
        sum=0
        prod=1

        while temp>0:
            r=temp%10
            temp=temp//10
            sum=sum+r
            prod*=r
        return prod-sum
