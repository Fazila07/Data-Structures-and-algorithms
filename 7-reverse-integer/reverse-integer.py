class Solution:
    def reverse(self, x: int) -> int:
        s=-1 if x<0 else 1
        x *= s
        rev=0
        num=x
        while num>0:
            last=num%10
            num=num//10
            if rev>(2**31-1)//10:
                return 0
            rev=rev*10+last
        return rev*s