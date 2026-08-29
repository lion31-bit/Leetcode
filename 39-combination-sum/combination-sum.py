class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        result=[]
        def back(index,total,sub):
            if total==target:
                result.append(sub.copy())
                return
            elif total>target or index>=n:
                return
            sub.append(nums[index])
            sun=nums[index]+total
            back(index,sun,sub)
            e=sub.pop()
            sun-=e
            back(index+1,sun,sub)
        back(0,0,[])
        return result

        