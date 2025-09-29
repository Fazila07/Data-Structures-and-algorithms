class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        w=sum(nums[:k])
        max_sum=w
        for i in range(k,len(nums)):
            w+=nums[i]-nums[i-k]
            if w>max_sum:
                max_sum=w
        return max_sum/k







