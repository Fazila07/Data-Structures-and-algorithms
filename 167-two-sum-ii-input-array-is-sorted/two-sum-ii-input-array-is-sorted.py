class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        length=0
        r = len(n)-1
        while length<r:
            s=n[length]+n[r]
            if s==target:
                return[length+1,r+1]
            elif s<target:
                length+=1
            else:
                r-=1