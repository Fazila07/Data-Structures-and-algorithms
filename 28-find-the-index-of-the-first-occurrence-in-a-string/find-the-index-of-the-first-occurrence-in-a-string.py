class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack==needle:
            return 0
        n=len(haystack)
        left=0
        right=len(needle)
        index=0
        while (left<n and right<n+1):
            sub=haystack[left:right]
            if sub==needle:
                return index
            index+=1
            left+=1
            right+=1
        return -1
            