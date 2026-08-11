class Solution(object):
    def twoSum(self, nums, target):
        left=0
        n=len(nums)
        right=n-1
        map=dict()
        for i in range(n):
            remain=target-nums[i]
            if remain in map:
                return [map[remain],i]
            map[nums[i]]=i

        
        