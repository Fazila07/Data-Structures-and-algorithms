class Solution:
    def compress(self, chars: List[str]) -> int:
        n=len(chars)
        left,right=0,0
        while right<n:
            char=chars[right]
            count=0
            while right<n and chars[right]==char:
                count+=1
                right+=1
            chars[left]=char
            left+=1
            if count>1:
                for i in str(count):
                    chars[left]=i
                    left+=1
        return left