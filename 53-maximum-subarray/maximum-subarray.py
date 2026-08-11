class Solution(object):
    def maxSubArray(self, nums):
        max_sum=float("-inf")
        n=len(nums)
        curr=0
        for i in range(n):
            curr=max(nums[i],curr+nums[i])
            if curr>max_sum:
                max_sum=curr
        return max(max_sum,curr)
        
        