# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

# Return the answer in an array.

 

# Example 1:

# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]



class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a=[]
        for i in nums:
            c=0
            for j in nums:
                if(i>j):
                    c=c+1
            a.append(c)
        return a