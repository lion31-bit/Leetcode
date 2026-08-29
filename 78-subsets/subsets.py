class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        result=[]
        def back(index,sub):
            if index>=n:
                result.append(sub.copy())
                return
            sub.append(nums[index])
            back(index+1,sub)
            sub.pop()
            back(index+1,sub)
        back(0,[])
        return result