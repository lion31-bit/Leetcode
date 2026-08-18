class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def solve(ind,total,bracket):
            if ind>=len(bracket):
                if total==0:
                    result.append("".join(bracket))
                return
            if total>len(bracket)//2:
                return
            elif total<0:
                return
            bracket[ind]="("
            sun=total+1
            solve(ind+1,sun,bracket)
            bracket[ind]=")"
            sun=total-1
            solve(ind+1,sun,bracket)
        solve(0,0,[""]*(n*2))
        return result
        