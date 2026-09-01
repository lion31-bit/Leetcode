class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums=[1,2,3,4,5,6,7,8,9]
        length=len(nums)
        result=[]
        def back(index,total,sub):
            if total==n and len(sub)==k:
                result.append(sub.copy())
                return
            elif index>=length or total>n or len(sub)>=k:
                return
            sub.append(nums[index])
            sun=total+nums[index]
            back(index+1,sun,sub)
            sub.pop()
            back(index+1,total,sub)
        back(0,0,[])
        return result

                
            

