class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        n=len(candidates)
        def back(index,total,subset):
            if total==target:
                result.append(subset.copy())
                return
            if total>target:
                return
            elif index>=n:
                return
            sun=total+candidates[index]
            subset.append(candidates[index])
            back(index,sun,subset)
            sun=total
            subset.pop()
            back(index+1,sun,subset)
        back(0,0,[])
        return result

        