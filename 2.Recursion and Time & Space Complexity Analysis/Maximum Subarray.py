# Given an integer array nums, find the with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        cur_sum=0
        max_sum=nums[0]

        for i in range(0,n):
            cur_sum+=nums[i]
            if max_sum<cur_sum:
                max_sum=cur_sum
            if cur_sum<0:
                cur_sum=0
        return max_sum
