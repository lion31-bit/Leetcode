class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count=0
        max_count=0
        n=len(nums)
        for i in range(0,n):
            if nums[i]==1:
                count+=1
                if count>max_count:
                    max_count=count
            elif nums[i]==0:
                count=0
        return max(count,max_count)

        
        