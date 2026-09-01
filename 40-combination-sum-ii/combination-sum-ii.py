class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        result=[]
        def back(index,total,sub):
            if total == target:
                result.append(sub.copy())
                return
            elif index>=n or total>target:
                return
            for i in range(index,n):
                if i>index and nums[i]==nums[i-1]:
                    continue
                sub.append(nums[i])
                sun=total+nums[i]
                back(i+1,sun,sub)
                sub.pop()
        back(0,0,[])
        return result