class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        nums=x
        result=0
        while nums!=0:
            divi=nums%10
            result=result*10+divi
            nums=nums//10
        return result==x



        
        