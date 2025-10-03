class Solution:
    def isUgly(self, n: int) -> bool:
        while(n>1):    #repeats the block of code until it true
            if(n%2==0):    
               n=n/2       #divide the given number with 2 and if the reminder is divisible 3 or 5 then its 
            elif(n%3==0):  #ugly number
               n=n/3
            elif(n%5==0):
               n=n/5
            else:
               return False
        if(n==1):   #as 1 is divisible by all numbers this is the mandate conditon
            return True
        else:
            return False