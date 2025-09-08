class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        maximum_length = 0
        prefix = 0
        seen = {0: -1}   # store first occurrence of each prefix sum

        for i in range(n):
            if nums[i] == 0:
                prefix -= 1
            else:
                prefix += 1

            if prefix in seen:
                maximum_length = max(maximum_length, i - seen[prefix])
            else:
                seen[prefix] = i

        return maximum_length
