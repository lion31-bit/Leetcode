class Solution(object):
    def rearrangeArray(self, nums):
        n=len(nums)
        result=[0]*n
        pos=0
        neg=1
        for i in range(n):
            if nums[i]>=0:
                result[pos]=nums[i]
                pos+=2
        for j in range(n):
            if nums[j]<0:
                result[neg]=nums[j]
                neg+=2
        return result
                
        
        