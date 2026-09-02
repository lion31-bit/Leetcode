class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        maps = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl','6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result=[]
        def back(index,sub):
            if index>=len(digits):
                result.append("".join(sub))
                return
            for ch in maps[digits[index]]:
                sub.append(ch)
                back(index+1,sub)
                sub.pop()
        back(0,[])
        return result
        