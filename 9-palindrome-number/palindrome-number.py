class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        rev=0
        original=x
        while x!=0:
            D=x%10
            rev=rev*10+D
            x=x//10
        return rev==original
