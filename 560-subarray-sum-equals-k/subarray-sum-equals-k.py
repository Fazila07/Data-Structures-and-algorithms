class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        prefix_sum=0
        prefix_num={0:1}
        for num in nums:
            prefix_sum+=num
            if(prefix_sum-k) in prefix_num:
                count+=prefix_num[prefix_sum-k]
            prefix_num[prefix_sum]=prefix_num.get(prefix_sum,0)+1
        return count

