class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        rev=0
        original=x
        while x!=0:
            digit=x%10 #to get last digit
            rev=rev*10+digit
            x=x//10
        return rev==original